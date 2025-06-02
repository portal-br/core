from plone.distribution.core import Distribution
from portalbrasil.core import __version__
from portalbrasil.core.utils import distributions as dist_utils

import pytest


class TestUtilsDistributions:
    @pytest.fixture(autouse=True)
    def _setup(self, portal):
        self.portal = portal

    def test_current_distribution(self):
        result = dist_utils.current_distribution()
        assert isinstance(result, Distribution)
        assert result.name == "testing"

    @pytest.mark.parametrize(
        "key,expected",
        [
            ("name", "testing"),
            ("title", "portalbrasil.core"),
            ("package_name", "portalbrasil.core.testing"),
            ("package_version", __version__),
        ],
    )
    def test_distribution_info(self, key, expected):
        result = dist_utils.distribution_info()
        assert isinstance(result, dict)
        assert result[key] == expected
