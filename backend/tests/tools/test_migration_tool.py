from portalbrasil.core import __version__
from portalbrasil.core.tools.migration import MigrationTool
from zope.component.hooks import site

import pytest


class TestMigrationTool:
    @pytest.fixture(autouse=True)
    def _setup(self, portal, current_versions):
        self.tool: MigrationTool = portal.portal_migration
        self.profile_version = current_versions.base

    def test_is_instance(self):
        """Test portal_migration uses our class."""
        assert isinstance(self.tool, MigrationTool)

    def test_getSoftwareVersion(self):
        """Test portal_migration.getSoftwareVersion."""

        assert self.tool.getSoftwareVersion() == __version__

    def test_getFileSystemVersion(self):
        """Test portal_migration.getFileSystemVersion."""

        assert self.tool.getFileSystemVersion() == self.profile_version

    def test_getInstanceVersion(self):
        """Test portal_migration.getFileSystemVersion."""

        assert self.tool.getInstanceVersion() == self.profile_version

    def test_listUpgrades(self):
        """Test portal_migration.listUpgrades."""
        assert isinstance(self.tool.list_steps(), list)

    def test_list_steps(self):
        """Test portal_migration.list_steps."""
        assert isinstance(self.tool.list_steps(), list)


class TestMigrationToolVersions:
    @pytest.fixture(autouse=True)
    def _setup(self, portal_class, current_versions):
        self.tool: MigrationTool = portal_class.portal_migration
        self.profile_version = current_versions.base

    @pytest.mark.parametrize(
        "key,expected",
        [
            [
                "core",
                {
                    "name": "portalbrasil.core",
                    "package_version": __version__,
                    "instance_version": "current_profile_version",
                    "fs_version": "current_profile_version",
                },
            ],
            ["Zope", "5.13"],
            ["CMFPlone", "6.1.1"],
        ],
    )
    def test_coreVersions(self, key: str, expected: str):
        """Test portal_migration.coreVersions."""
        if key == "core":
            expected["instance_version"] = self.profile_version
            expected["fs_version"] = self.profile_version
        info = self.tool.coreVersions()
        assert isinstance(info, dict)
        assert info[key] == expected

    @pytest.mark.parametrize(
        "key",
        [
            "CMF",
            "CMFPlone",
            "Debug mode",
            "PIL",
            "Platform",
            "Plone File System",
            "Plone Instance",
            "core",
            "Python",
            "Zope",
        ],
    )
    def test_coreVersions_keys(self, key: str):
        """Test portal_migration.coreVersions."""
        info = self.tool.coreVersions()
        assert key in info

    @pytest.mark.parametrize(
        "key",
        [
            "CMF",
            "CMFPlone",
            "Debug mode",
            "PIL",
            "Platform",
            "Plone File System",
            "Plone Instance",
            "core",
            "Python",
            "Zope",
        ],
    )
    def test_coreVersions_keys_without_site_hook(self, key: str):
        """Test access to the tool without the site hook being set."""
        with site(None):
            info = self.tool.coreVersions()
        assert key in info
