from AccessControl.class_init import InitializeClass
from App.config import getConfiguration
from collections.abc import Generator
from contextlib import contextmanager
from io import StringIO
from plone import api
from plone.base.interfaces import IMigrationTool
from portalbrasil.core import FRIENDLY_NAME
from portalbrasil.core import __version__
from portalbrasil.core.utils import gs as gs_utils
from portalbrasil.core.utils import packages as pkg_utils
from Products.CMFCore.utils import registerToolInterface
from Products.CMFPlone.MigrationTool import Addon
from Products.CMFPlone.MigrationTool import AddonList
from Products.CMFPlone.MigrationTool import MigrationTool as BaseTool
from Products.GenericSetup.tool import SetupTool
from typing import Any
from ZODB.POSException import ConflictError
from zope.interface import implementer

import logging
import sys
import transaction


@contextmanager
def get_logger(stream: StringIO) -> Generator[logging.Logger]:
    from portalbrasil.core import logger

    handler = logging.StreamHandler(stream)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    gslogger = logging.getLogger("GenericSetup")
    gslogger.addHandler(handler)
    try:
        yield logger
    finally:
        # Remove new handler
        logger.removeHandler(handler)
        gslogger.removeHandler(handler)


ADDON_LIST = AddonList([
    Addon(profile_id="Products.CMFEditions:CMFEditions"),
    Addon(
        profile_id="Products.CMFPlacefulWorkflow:CMFPlacefulWorkflow",
        check_module="Products.CMFPlacefulWorkflow",
    ),
    Addon(profile_id="Products.PlonePAS:PlonePAS"),
    Addon(profile_id="plone.app.caching:default", check_module="plone.app.caching"),
    Addon(profile_id="plone.app.contenttypes:default"),
    Addon(profile_id="plone.app.dexterity:default"),
    Addon(
        profile_id="plone.app.discussion:default",
        check_module="plone.app.discussion",
    ),
    Addon(profile_id="plone.app.event:default"),
    Addon(profile_id="plone.app.iterate:default", check_module="plone.app.iterate"),
    Addon(
        profile_id="plone.app.multilingual:default",
        check_module="plone.app.multilingual",
    ),
    Addon(profile_id="plone.app.querystring:default"),
    Addon(profile_id="plone.app.theming:default"),
    Addon(profile_id="plone.app.users:default"),
    Addon(profile_id="plone.restapi:default"),
    Addon(profile_id="plone.session:default"),
    Addon(profile_id="plone.staticresources:default"),
    Addon(profile_id="plone.volto:default"),
    Addon(profile_id="plonetheme.barceloneta:default"),
    Addon(profile_id="plonegovbr.brfields:default"),
])


@implementer(IMigrationTool)
class MigrationTool(BaseTool):
    profile: str = "portalbrasil.core:base"
    package_name: str = "portalbrasil.core"

    @property
    def setup(self) -> SetupTool:
        return api.portal.get_tool("portal_setup")

    def getInstanceVersion(self) -> str:
        # The version this instance of plone is on.
        setup = self.setup
        version = setup.getLastVersionForProfile(self.profile)
        if isinstance(version, tuple):
            version = ".".join(version)

        _version = getattr(self, "_version", None)
        if _version is None:
            self._version = False

        if version == "unknown":
            version = (
                gs_utils.sanitize_gs_version(_version)
                if _version
                else setup.getVersionForProfile(self.profile)
            )
            version = setup.getVersionForProfile(self.profile)
            self.setInstanceVersion(version)
        return version

    def setInstanceVersion(self, version: str) -> None:
        # The version this instance of portalbrasil.core is on.
        setup = self.setup
        setup.setLastVersionForProfile(self.profile, version)
        self._version = False

    def getFileSystemVersion(self) -> str | None:
        # The version this instance of portalbrasil.core is on.
        setup = self.setup
        try:
            return setup.getVersionForProfile(self.profile)
        except KeyError:
            pass
        return None

    def getSoftwareVersion(self) -> str:
        # The software version.
        return __version__

    def listUpgrades(self):
        setup = self.setup
        fs_version = self.getFileSystemVersion()
        upgrades = setup.listUpgrades(self.profile, dest=fs_version)
        return upgrades

    def list_steps(self) -> list:
        upgrades = self.listUpgrades()
        steps = []
        for u in upgrades:
            if isinstance(u, list):
                steps.extend(u)
            else:
                steps.append(u)
        return steps

    def coreVersions(self) -> dict[str, Any]:
        # Useful core information.
        plone_version = pkg_utils.package_version("Products.CMFPlone")
        return {
            "Python": sys.version,
            "Zope": pkg_utils.package_version("Zope"),
            "Platform": sys.platform,
            f"{FRIENDLY_NAME}": self.getSoftwareVersion(),
            f"{FRIENDLY_NAME} Instance": self.getInstanceVersion(),
            f"{FRIENDLY_NAME} File System": self.getFileSystemVersion(),
            "plone.restapi": pkg_utils.package_version("plone.restapi"),
            "plone.volto": pkg_utils.package_version("plone.volto"),
            "CMFPlone": plone_version,
            "Plone": plone_version,
            "CMF": pkg_utils.package_version("Products.CMFCore"),
            "Debug mode": "Yes" if getConfiguration().debug_mode else "No",
            "PIL": pkg_utils.package_version("pillow"),
        }

    def _upgrade_run_steps(
        self, steps: list, logger: logging.Logger, swallow_errors: bool
    ) -> None:
        setup = self.setup
        for step in steps:
            try:
                step_title = step["title"]
                step["step"].doStep(setup)
                setup.setLastVersionForProfile(self.profile, step["dest"])
                logger.info(f"Ran upgrade step: {step_title}")
            except (ConflictError, KeyboardInterrupt):
                raise
            except Exception:
                logger.error("Upgrade aborted. Error:\n", exc_info=True)

                if not swallow_errors:
                    raise
                else:
                    # abort transaction to safe the zodb
                    transaction.abort()
                    break

    def _upgrade_recatalog(self, logger: logging.Logger, swallow_errors: bool) -> None:
        if not self.needRecatalog():
            return
        logger.info("Recatalog needed. This may take a while...")
        try:
            catalog = self.portal_catalog
            # Reduce threshold for the reindex run
            old_threshold = catalog.threshold
            pg_threshold = getattr(catalog, "pgthreshold", 0)
            catalog.pgthreshold = 300
            catalog.threshold = 2000
            catalog.refreshCatalog(clear=1)
            catalog.threshold = old_threshold
            catalog.pgthreshold = pg_threshold
            self._needRecatalog = 0
        except (ConflictError, KeyboardInterrupt):
            raise
        except Exception:
            logger.error(
                "Exception was thrown while cataloging:\n",
                exc_info=True,
            )
            if not swallow_errors:
                raise

    def _upgrade_roles(self, logger: logging.Logger, swallow_errors: bool) -> None:
        if self.needUpdateRole():
            logger.info("Role update needed. This may take a while...")
            try:
                self.portal_workflow.updateRoleMappings()
                self._needUpdateRole = 0
            except (ConflictError, KeyboardInterrupt):
                raise
            except Exception:
                logger.error(
                    "Exception was thrown while updating role mappings",
                    exc_info=True,
                )
                if not swallow_errors:
                    raise

    def upgrade(
        self, REQUEST=None, dry_run: bool = False, swallow_errors: bool = True
    ) -> str:
        # Perform the upgrade.
        # This sets the profile version if it wasn't set yet
        version = self.getInstanceVersion()
        steps = self.list_steps()
        stream = StringIO()
        with get_logger(stream) as logger:
            if dry_run:
                logger.info("Dry run selected.")

            logger.info(f"Starting the migration from version: {version}")
            self._upgrade_run_steps(steps, logger, swallow_errors)
            logger.info("End of upgrade path, main migration has finished.")

            if self.needUpgrading():
                logger.error("The upgrade path did NOT reach current version.")
                logger.error("Migration has failed")
            else:
                logger.info("Starting upgrade of core addons.")
                ADDON_LIST.upgrade_all(self)
                logger.info("Done upgrading core addons.")

                # do this once all the changes have been done
                self._upgrade_recatalog(logger, swallow_errors=swallow_errors)
                self._upgrade_roles(logger, swallow_errors=swallow_errors)
                logger.info("Your Plone instance is now up-to-date.")

            if dry_run:
                logger.info("Dry run selected, transaction aborted")
                transaction.abort()

        return stream.getvalue()


InitializeClass(MigrationTool)
registerToolInterface("portal_migration", IMigrationTool)
