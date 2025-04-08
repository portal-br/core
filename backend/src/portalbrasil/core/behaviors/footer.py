from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.schema import JSONField
from plone.supermodel import model
from portalbrasil.core import _
from zope.interface import provider
from zope.schema import TextLine

import json


OBJECT_LIST_DEFAULT_VALUE = []

OBJECT_LIST = json.dumps({
    "type": "array",
    "items": {
        "type": "object",
    },
})


@provider(IFormFieldProvider)
class ISiteFooterCustomizationSettings(model.Schema):
    """Site/Subsite footer properties behavior."""

    model.fieldset(
        "footer",
        label=_("Footer customizations"),
        fields=[
            "footer_logos",
            "footer_logos_container_width",
            "footer_logos_size",
            "footer_links",
        ],
    )

    directives.widget(
        "footer_logos",
        frontendOptions={
            "widget": "object_list",
            "widgetProps": {"schemaName": "footerLogos"},
        },
    )
    footer_logos = JSONField(
        title=_("Footer logos"),
        schema=OBJECT_LIST,
        default=OBJECT_LIST_DEFAULT_VALUE,
        required=False,
        widget="",
    )

    directives.widget(
        "footer_logos_container_width",
        frontendOptions={
            "widget": "blockWidth",
            "widgetProps": {
                "filterActions": ["default", "layout"],
                "actions": [
                    {
                        "name": "default",
                        "label": "Default",
                    },
                    {
                        "name": "layout",
                        "label": "Layout",
                    },
                ],
            },
        },
    )
    footer_logos_container_width = TextLine(
        title=_("Footer logos container width"),
        default="default",
        required=False,
    )

    directives.widget(
        "footer_logos_size",
        frontendOptions={
            "widget": "size",
            "widgetProps": {"filterActions": ["s", "l"]},
        },
    )
    footer_logos_size = TextLine(
        title=_("Footer logos size"),
        default="s",
        required=False,
    )

    directives.widget(
        "footer_links",
        frontendOptions={
            "widget": "object_list",
            "widgetProps": {"schemaName": "footerLinks"},
        },
    )
    footer_links = JSONField(
        title=_("Footer links"),
        schema=OBJECT_LIST,
        default=OBJECT_LIST_DEFAULT_VALUE,
        required=False,
        widget="",
    )
