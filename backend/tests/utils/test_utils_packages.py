from portalbrasil.core.utils import packages as pkg_utils


class TestUtilsPackages:
    def test_package_version(self):
        from portalbrasil.core import __version__

        result = pkg_utils.package_version("portalbrasil.core")
        assert result == __version__
