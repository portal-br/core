"""Module where all interfaces, events and exceptions live."""

from Products.CMFPlone.MigrationTool import AddonList
from zope.interface import Interface
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IBrowserLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IAddonList(Interface):
    """List of add ons managed by migration tool."""

    addon_list: AddonList
