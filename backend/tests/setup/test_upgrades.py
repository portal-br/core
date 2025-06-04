from portalbrasil.core import PACKAGE_NAME
from Products.GenericSetup.tool import SetupTool

import pytest


@pytest.fixture
def set_profile_version(setup_tool: SetupTool):
    """Fixture to set the profile version."""

    def _set_version(profile_id: str, version: str):
        setup_tool.setLastVersionForProfile(profile_id, version)

    return _set_version


class TestUpgrades:
    profile_name: str = f"{PACKAGE_NAME}:base"

    @pytest.fixture(autouse=True)
    def _setup(self, portal, setup_tool):
        self.portal = portal
        self.tool: SetupTool = setup_tool

    @pytest.mark.parametrize(
        "profile_src,profile_dest,steps",
        [
            ("1000", "1001", 2),
            ("1001", "1002", 2),
        ],
    )
    def test_upgrade_steps(
        self, set_profile_version, profile_src: str, profile_dest: str, steps: int
    ):
        """Test latest version of default profile."""
        # Set profile to source version
        set_profile_version(self.profile_name, profile_src)
        # List upgrade steps
        steps_list = self.tool.listUpgrades(
            self.profile_name, dest=profile_dest, simple=True
        )
        assert len(steps_list) == steps
