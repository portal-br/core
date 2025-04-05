from plone import api
from plone.restapi.services import Service
from portalbrasil.core import FRIENDLY_NAME
from portalbrasil.core.tools.migration import MigrationTool
from portalbrasil.core.utils.distributions import distribution_info


class SystemGet(Service):
    def reply(self) -> dict:
        migration_tool: MigrationTool = api.portal.get_tool("portal_migration")
        core_versions = migration_tool.coreVersions()
        gs_fs = core_versions.get(f"{FRIENDLY_NAME} File System")
        gs_instance = core_versions.get(f"{FRIENDLY_NAME} Instance")
        return {
            "@id": f"{self.context.absolute_url()}/@system",
            "distribution": distribution_info(),
            "portalbrasil": {
                "version": core_versions.get("PortalBrasil"),
                "profile_version_installed": gs_instance,
                "profile_version_file_system": gs_fs,
            },
            "zope_version": core_versions.get("Zope"),
            "plone_version": core_versions.get("CMFPlone"),
            "plone_restapi_version": core_versions.get("plone.restapi"),
            "plone_volto_version": core_versions.get("plone.volto"),
            "python_version": core_versions.get("Python"),
            "cmf_version": core_versions.get("CMF"),
            "pil_version": core_versions.get("PIL"),
            "debug_mode": core_versions.get("Debug mode"),
            "upgrade": gs_fs != gs_instance,
        }
