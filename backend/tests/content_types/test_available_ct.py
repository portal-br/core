from Products.CMFPlone.TypesTool import TypesTool

import pytest


class TestCTAvailable:
    @pytest.fixture(autouse=True)
    def _setup(self, portal_class):
        self.portal = portal_class
        self.types_tool: TypesTool = portal_class.portal_types

    @pytest.mark.parametrize(
        "portal_type,title,klass,addable",
        [
            ("Plone Site", "Plone Site", "Products.CMFPlone.Portal.PloneSite", False),
            ("Document", "Page", "plone.volto.content.FolderishDocument", True),
            ("News Item", "News Item", "plone.volto.content.FolderishNewsItem", True),
            ("Event", "Event", "plone.volto.content.FolderishEvent", True),
            ("Image", "Image", "plone.app.contenttypes.content.Image", True),
            ("Folder", "Folder", "plone.app.contenttypes.content.Folder", False),
            (
                "Collection",
                "Collection",
                "plone.app.contenttypes.content.Collection",
                False,
            ),
        ],
    )
    def test_portal_type(self, portal_type: str, title: str, klass: str, addable: bool):
        """Test if a portal_type is installed."""
        from plone.dexterity.fti import DexterityFTI

        fti = self.types_tool.getTypeInfo(portal_type)
        assert isinstance(fti, DexterityFTI)
        assert fti.title == title
        assert fti.klass == klass
        assert fti.global_allow is addable
