from plone.dexterity.fti import DexterityFTI

import pytest


class TestContentTypeFTI:
    portal_type: str = "Event"

    @pytest.fixture(autouse=True)
    def _setup(self, portal, get_fti):
        self.portal = portal
        self.fti: DexterityFTI = get_fti(self.portal_type)

    @pytest.mark.parametrize(
        "attr,expected",
        [
            ("title", "Event"),
            ("klass", "plone.volto.content.FolderishEvent"),
            ("global_allow", True),
        ],
    )
    def test_fti(self, attr: str, expected):
        """Test FTI values."""
        fti = self.fti

        assert isinstance(fti, DexterityFTI)
        assert getattr(fti, attr) == expected

    @pytest.mark.parametrize(
        "name,expected",
        [
            ("plone.eventbasic", True),
            ("plone.eventrecurrence", True),
            ("plone.eventlocation", True),
            ("plone.eventattendees", True),
            ("plone.eventcontact", True),
            ("plone.basic", True),
            ("volto.preview_image_link", True),
            ("plone.categorization", True),
            ("plone.publication", True),
            ("plone.ownership", True),
            ("plone.shortname", True),
            ("volto.navtitle", True),
            ("plone.excludefromnavigation", True),
            ("plone.allowdiscussion", True),
            ("plone.relateditems", True),
            ("volto.blocks", True),
            ("plone.constraintypes", True),
            ("plone.locking", True),
            ("plone.namefromtitle", True),
            ("plone.textindexer", True),
            ("plone.versioning", True),
            ("plone.locking", True),
            ("plone.translatable", True),
        ],
    )
    def test_behavior(self, name: str, expected: bool):
        """Test behavior is present or not."""
        fti = self.fti
        behaviors = fti.behaviors
        assert (name in behaviors) is expected
