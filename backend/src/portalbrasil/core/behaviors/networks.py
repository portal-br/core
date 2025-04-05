from plone.autoform import directives
from plone.autoform.interfaces import IFormFieldProvider
from plone.schema import JSONField
from plone.supermodel import model
from portalbrasil.core import _
from zope.interface import provider

import json


OBJECT_LIST_DEFAULT_VALUE = []

OBJECT_LIST = json.dumps({
    "type": "array",
    "items": {
        "type": "object",
    },
})


@provider(IFormFieldProvider)
class ISiteSocialNetworks(model.Schema):
    """Site/Subsite social networks configuration."""

    model.fieldset(
        "social_networks",
        label=_("Social Networks"),
        fields=[
            "network_links",
        ],
    )

    directives.widget(
        "network_links",
        frontendOptions={
            "widget": "object_list",
            "widgetProps": {"schemaName": "socialNetworks"},
        },
    )
    network_links = JSONField(
        title=_("Social Networks"),
        schema=OBJECT_LIST,
        default=OBJECT_LIST_DEFAULT_VALUE,
        required=False,
        widget="",
    )
