from contextlib import suppress
from portalbrasil.core import logger
from portalbrasil.core.utils import gs
from portalbrasil.core.utils import types
from Products.GenericSetup.tool import SetupTool


def remove_behavior_social_networks(setup_tool: SetupTool):
    """Remove portalbrasil.social_networks do tipo Plone Site."""
    behavior = "portalbrasil.social_networks"
    portal_type = "Plone Site"
    fti = types.get_fti(portal_type)
    behaviors = list(fti.behaviors)
    with suppress(ValueError):
        behaviors.remove(behavior)
    fti.behaviors = tuple(behaviors)
    logger.info(f"Removido o behavior {behavior} do tipo {portal_type}")


def instala_socialmedia(setup_tool: SetupTool):
    """Instala plonegovbr.socialmedia."""
    package = "plonegovbr.socialmedia"
    gs.install_package(package)
    logger.info(f"Instalado complemento {package}")
