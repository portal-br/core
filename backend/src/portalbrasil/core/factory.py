from plone.base.interfaces.installable import INonInstallable
from plone.distribution.api import site as site_api
from zope.component.hooks import setSite
from zope.interface import implementer


_DEFAULT_PROFILE = "portalbrasil.core:base"
_DEPENDENCIES_PROFILE = "portalbrasil.core:dependencies"
_PLONE_PACKAGES = [
    "CMFDefault",
    "Products.CMFDefault",
    "CMFPlone",
    "Products.CMFPlone",
    "Products.CMFPlone.migrations",
    "CMFTopic",
    "Products.CMFTopic",
    "CMFUid",
    "Products.CMFUid",
    "DCWorkflow",
    "Products.DCWorkflow",
    "PasswordResetTool",
    "Products.PasswordResetTool",
    "PlonePAS",
    "Products.PlonePAS",
    "PloneLanguageTool",
    "Products.PloneLanguageTool",
    "MimetypesRegistry",
    "Products.MimetypesRegistry",
    "PortalTransforms",
    "Products.PortalTransforms",
    "CMFDiffTool",
    "Products.CMFDiffTool",
    "CMFEditions",
    "Products.CMFEditions",
    "Products.NuPlone",
    "borg.localrole",
    "plone.app.dexterity",
    "plone.app.event",
    "plone.app.intid",
    "plone.app.linkintegrity",
    "plone.app.querystring",
    "plone.app.registry",
    "plone.app.referenceablebehavior",
    "plone.app.relationfield",
    "plone.app.theming",
    "plone.app.users",
    "plone.app.z3cform",
    "plone.formwidget.recurrence",
    "plone.keyring",
    "plone.outputfilters",
    "plone.portlet.static",
    "plone.portlet.collection",
    "plone.protect",
    "plone.resource",
    "plonetheme.barceloneta",
    "plone.restapi",
    "plone.volto",
    "plonegovbr.brfields",
]
_PLONE_PROFILES = [
    "Products.CMFDiffTool:CMFDiffTool",
    "Products.CMFEditions:CMFEditions",
    "Products.CMFPlone:dependencies",
    "Products.CMFPlone:testfixture",
    "Products.NuPlone:uninstall",
    "Products.MimetypesRegistry:MimetypesRegistry",
    "Products.PasswordResetTool:PasswordResetTool",
    "Products.PortalTransforms:PortalTransforms",
    "Products.PloneLanguageTool:PloneLanguageTool",
    "Products.PlonePAS:PlonePAS",
    "borg.localrole:default",
    "plone.browserlayer:default",
    "plone.keyring:default",
    "plone.outputfilters:default",
    "plone.portlet.static:default",
    "plone.portlet.collection:default",
    "plone.protect:default",
    "plone.app.contenttypes:default",
    "plone.app.dexterity:default",
    "plone.app.event:default",
    "plone.app.linkintegrity:default",
    "plone.app.registry:default",
    "plone.app.relationfield:default",
    "plone.app.theming:default",
    "plone.app.users:default",
    "plone.app.versioningbehavior:default",
    "plone.app.z3cform:default",
    "plone.formwidget.recurrence:default",
    "plone.resource:default",
    "plone.restapi:default",
    "plone.volto:default",
    "plonegovbr.brfields:default",
    "plonegovbr.brfields:demo",
]


@implementer(INonInstallable)
class HiddenProfiles:
    def getNonInstallableProducts(self):
        return [*_PLONE_PACKAGES]

    def getNonInstallableProfiles(self):
        """Hide uninstall profile from site-creation and quickinstaller."""
        return [_DEFAULT_PROFILE, _DEPENDENCIES_PROFILE, *_PLONE_PROFILES]


def add_site(
    context,
    site_id: str,
    title: str = "PortalBrasil: Site",
    description: str = "",
    profile_id: str = _DEFAULT_PROFILE,
    snapshot: bool = False,
    content_profile_id: str | None = None,
    extension_ids: tuple[str] = (),
    setup_content: bool = False,
    default_language: str = "pt-br",
    portal_timezone: str = "UTC",
    distribution: str = "volto",
    **kwargs,
):
    """Add a PloneSite to the context."""

    # Pass all arguments and keyword arguments in the answers,
    # But the 'distribution_name' is not needed there.
    answers = {
        "site_id": site_id,
        "title": title,
        "description": description,
        "profile_id": profile_id,
        "snapshot": snapshot,
        "content_profile_id": content_profile_id,
        "extension_ids": extension_ids,
        "setup_content": setup_content,
        "default_language": default_language,
        "portal_timezone": portal_timezone,
    }
    answers.update(kwargs)
    site = site_api._create_site(
        context=context,
        distribution_name=distribution,
        answers=answers,
        profile_id=profile_id,
    )
    setSite(site)
    return site
