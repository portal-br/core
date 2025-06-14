from plone.dexterity.fti import DexterityFTI

import pytest


class TestCTPloneSite:
    portal_type: str = "Plone Site"

    @pytest.fixture(autouse=True)
    def _setup(self, portal, get_fti):
        self.portal = portal
        self.fti: DexterityFTI = get_fti(self.portal_type)

    @pytest.mark.parametrize(
        "attr,expected",
        [
            ("title", "Plone Site"),
            ("klass", "Products.CMFPlone.Portal.PloneSite"),
            ("global_allow", False),
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
            ("plone.dublincore", True),
            ("plone.richtext", False),
            ("plone.relateditems", True),
            ("plone.locking", True),
            ("plone.excludefromnavigation", True),
            ("plone.tableofcontents", True),
            ("portalbrasil.header", True),
            ("portalbrasil.footer", True),
            ("portalbrasil.social_networks", False),
            ("plonegovbr.socialmedia", False),
            ("volto.blocks", True),
            ("volto.preview_image_link", True),
        ],
    )
    def test_behavior(self, name: str, expected: bool):
        """Test behavior is present or not."""
        fti = self.fti
        behaviors = fti.behaviors
        assert (name in behaviors) is expected
