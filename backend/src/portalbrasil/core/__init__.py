"""Init and utils."""

from zope.i18nmessageid import MessageFactory

import logging


__version__ = "1.0.0a3"

PACKAGE_NAME = "portalbrasil.core"
FRIENDLY_NAME = "PortalBrasil"

_ = MessageFactory(PACKAGE_NAME)

logger = logging.getLogger(PACKAGE_NAME)


def initialize(context):
    from portalbrasil.core.tools import migration
    from Products.CMFPlone.utils import ToolInit

    tools = (migration.MigrationTool,)
    # Register tools and content
    ToolInit(
        "Plone Tool",
        tools=tools,
        icon="tool.gif",
    ).initialize(context)
