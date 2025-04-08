from AccessControl.SecurityManagement import newSecurityManager
from OFS.Application import Application
from pathlib import Path
from portalbrasil.core import logger
from portalbrasil.core.factory import add_site
from portalbrasil.core.interfaces import IBrowserLayer
from Products.CMFPlone.Portal import PloneSite
from Testing.makerequest import makerequest
from zope.interface import directlyProvidedBy
from zope.interface import directlyProvides
from zope.interface.interface import InterfaceClass
from ZPublisher.HTTPRequest import HTTPRequest

import json
import logging
import os
import transaction


truthy = frozenset(("t", "true", "y", "yes", "on", "1"))


def asbool(s):
    """Return the boolean value ``True`` if the case-lowered value of string
    input ``s`` is a :term:`truthy string`. If ``s`` is already one of the
    boolean values ``True`` or ``False``, return it."""
    if s is None:
        return False
    if isinstance(s, bool):
        return s
    s = str(s).strip()
    return s.lower() in truthy


def parse_answers(answers_file: Path, answers_env: dict) -> dict:
    answers = json.loads(answers_file.read_text())
    for key in answers:
        env_value = answers_env.get(key, "")
        if key == "setup_content" and env_value.strip():
            env_value = asbool(env_value)
        elif not env_value:
            continue
        # Override answers_file value
        answers[key] = env_value
    return answers


def _prepare_loggers():
    logging.basicConfig(format="%(message)s")
    logger.setLevel(logging.INFO)
    # Silence some loggers
    for logger_name in [
        "GenericSetup.componentregistry",
        "Products.MimetypesRegistry.MimeTypesRegistry",
    ]:
        logging.getLogger(logger_name).setLevel(logging.ERROR)


def _prepare_request(app: Application, package_iface: InterfaceClass | None = None):
    request: HTTPRequest = app.REQUEST
    ifaces = [IBrowserLayer]
    if package_iface:
        ifaces.append(package_iface)
    for iface in directlyProvidedBy(request):
        ifaces.append(iface)

    directlyProvides(request, *ifaces)


def _prepare_user(app: Application):
    admin = app.acl_users.getUserById("admin")
    admin = admin.__of__(app.acl_users)
    newSecurityManager(None, admin)


def create_site(
    app: Application,
    env_answers: dict,
    answers_file: Path,
    package_iface: InterfaceClass | None = None,
) -> PloneSite:
    _prepare_loggers()
    app = makerequest(app)
    _prepare_request(app, package_iface)
    _prepare_user(app)
    distribution = os.getenv("DISTRIBUTION")
    delete_existing = asbool(os.getenv("DELETE_EXISTING"))

    # Load site creation parameters
    answers = parse_answers(answers_file, env_answers)
    if "distribution" not in answers:
        answers["distribution"] = distribution
    else:
        distribution = answers["distribution"]
    site_id = answers["site_id"]

    logger.info(f"Creating a new PortalBrasil site  @ {site_id}")
    logger.info(
        f" - Using the {distribution} distribution and answers from {answers_file}"
    )

    if site_id in app.objectIds():
        if delete_existing:
            with transaction.manager:
                app.manage_delObjects([site_id])
            logger.info(f" - Deleted existing site with id {site_id}")
        else:
            logger.info(
                " - Stopping site creation, as there is already a site with id "
                f"{site_id} at the instance. Set DELETE_EXISTING=1 to delete "
                "the existing site before creating a new one."
            )

    app._p_jar.sync()
    if site_id not in app.objectIds():
        with transaction.manager:
            site = add_site(app, **answers)
        logger.info(f" - Site {site.id} created!")
    else:
        site = app[site_id]
    return site
