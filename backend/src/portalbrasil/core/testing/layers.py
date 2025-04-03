from plone.app.testing.interfaces import DEFAULT_LANGUAGE
from plone.app.testing.interfaces import PLONE_SITE_ID
from plone.app.testing.interfaces import SITE_OWNER_NAME
from plone.app.testing.interfaces import SITE_OWNER_PASSWORD
from plone.app.testing.interfaces import TEST_USER_ID
from plone.app.testing.interfaces import TEST_USER_NAME
from plone.app.testing.interfaces import TEST_USER_PASSWORD
from plone.app.testing.interfaces import TEST_USER_ROLES
from plone.app.testing.layers import PloneFixture
from plone.testing import zope


PLONE_SITE_TITLE = "PortalBrasil Site"


class PortalBrasilFixture(PloneFixture):
    internal_packages: tuple[str] = (
        "plone.restapi",
        "plone.volto",
        "portalbrasil.core",
    )

    @property
    def products(self) -> tuple[tuple[str, dict], ...]:
        products = list(super().products)
        for package in self.internal_packages:
            products.append((package, {"loadZCML": True}))
        return tuple(products)

    def setUpDefaultContent(self, app):
        app["acl_users"].userFolderAddUser(
            SITE_OWNER_NAME, SITE_OWNER_PASSWORD, ["Manager"], []
        )

        zope.login(app["acl_users"], SITE_OWNER_NAME)

        # Create the site with the default set of extension profiles
        from portalbrasil.core.factory import add_site

        add_site(
            app,
            PLONE_SITE_ID,
            title=PLONE_SITE_TITLE,
            setup_content=False,
            default_language=DEFAULT_LANGUAGE,
            extension_ids=self.extensionProfiles,
        )
        pas = app[PLONE_SITE_ID]["acl_users"]
        pas.source_users.addUser(TEST_USER_ID, TEST_USER_NAME, TEST_USER_PASSWORD)
        for role in TEST_USER_ROLES:
            pas.portal_role_manager.doAssignRoleToPrincipal(TEST_USER_ID, role)

        # Log out again
        zope.logout()
