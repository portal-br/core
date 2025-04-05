from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.namedfile.field import NamedBlobImage
from plone.schema import JSONField
from plone.supermodel import model
from portalbrasil.core import _
from zope.interface import provider
from zope.schema import Bool

import json


OBJECT_LIST_DEFAULT_VALUE = []

OBJECT_LIST = json.dumps({
    "type": "array",
    "items": {
        "type": "object",
    },
})


@provider(IFormFieldProvider)
class ISiteHeaderCustomizationSettings(model.Schema):
    """Site/Subsite Header properties behavior."""

    model.fieldset(
        "header",
        label=_("Cabeçalho"),
        fields=[
            "logo",
            "has_fat_menu",
            "header_actions",
        ],
    )

    logo = NamedBlobImage(
        title=_("label_site_logo", default="Site Logo"),
        description=_(
            "help_site_logo",
            default="If the site or subsite has a logo, please upload it here.",
        ),
        required=False,
    )

    has_fat_menu = Bool(
        title=_("label_enable_fat_menu", default="Enable Fat Menu"),
        description=_(
            "help_enable_fat_menu",
            default="If enabled, the fat menu will be shown.",
        ),
        required=False,
        default=True,
    )

    directives.widget(
        "header_actions",
        frontendOptions={
            "widget": "object_list",
            "widgetProps": {"schemaName": "headerActions"},
        },
    )
    header_actions = JSONField(
        title=_("Site Actions"),
        description=_(
            "help_header_actions",
            default="The site actions are the links that show in the top right side"
            " of the header.",
        ),
        schema=OBJECT_LIST,
        default=OBJECT_LIST_DEFAULT_VALUE,
        required=False,
        widget="",
    )
