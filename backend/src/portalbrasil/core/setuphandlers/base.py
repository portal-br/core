from plone import api
from Products.CMFPlone import setuphandlers
from Products.CMFPlone.Portal import PloneSite
from Products.GenericSetup.tool import SetupTool
from zope.component.hooks import getSite


_DEFAULT_PROFILE = "portalbrasil.core:base"


def get_setup_tool() -> SetupTool:
    """Return SetupTool."""
    return api.portal.get_tool("portal_setup")


def purge_profile_versions(portal: PloneSite):
    """Purge profile dependency versions."""
    setup = api.portal.get_tool("portal_setup")
    setup._profile_upgrade_versions = {}


def set_profile_version(portal: PloneSite):
    """Set profile version."""
    mt = api.portal.get_tool("portal_migration")
    mt.setInstanceVersion(mt.getFileSystemVersion())
    st = get_setup_tool()
    version = st.getVersionForProfile(_DEFAULT_PROFILE)
    st.setLastVersionForProfile(_DEFAULT_PROFILE, version)


def import_final_steps(context: SetupTool):
    """Final Plone import steps.

    This was an import step, but is now registered as post_handler
    specifically for our main 'plone' (profiles/default) profile.
    """
    site = getSite()

    # Unset all profile upgrade versions in portal_setup.  Our default
    # profile should only be applied when creating a new site, so this
    # list of versions should be empty.  But some tests apply it too.
    # This should not be done as it should not be needed.  The profile
    # is a base profile, which means all import steps are run in purge
    # mode.  So for example an extra workflow added by
    # plone.app.discussion is purged.  When plone.app.discussion is
    # still in the list of profile upgrade versions, with the default
    # dependency strategy it will not be reapplied again, which leaves
    # you with a site that misses stuff.  So: when applying our
    # default profile, start with a clean slate in these versions.
    purge_profile_versions(site)

    # Set out default profile version.
    set_profile_version(site)
    # Install our core dependencies
    st = get_setup_tool()
    st.runAllImportStepsFromProfile("profile-portalbrasil.core:dependencies")

    # Install package dependencies
    for profile_id in (
        "plone.app.contenttypes:default",
        "plone.restapi:default",
        "plone.volto:default",
        "plonegovbr.brfields:default",
    ):
        st.runAllImportStepsFromProfile(f"profile-{profile_id}")

    setuphandlers.replace_local_role_manager(site)
    setuphandlers.addCacheHandlers(site)

    setuphandlers.first_weekday_setup(context)
    setuphandlers.timezone_setup(context)
