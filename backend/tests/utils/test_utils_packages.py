from portalbrasil.core import __version__
from portalbrasil.core.utils import packages as pkg_utils

import pytest


class TestUtilsPackages:
    @pytest.mark.parametrize(
        "package_name,expected",
        [
            ("portalbrasil.core", __version__),
            ("portalbrasil.core.testing", __version__),
            ("", "-"),
        ],
    )
    def test_package_version(self, package_name: str, expected: str):
        result = pkg_utils.package_version(package_name)
        assert result == expected
