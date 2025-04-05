from plone.distribution.core import Distribution
from portalbrasil.core.utils import distributions as dist_utils

import pytest


class TestUtilsDistributions:
    @pytest.fixture(autouse=True)
    def _setup(self, portal):
        self.portal = portal

    def test_current_distribution(self):
        result = dist_utils.current_distribution()
        assert isinstance(result, Distribution)
        assert result.name == "volto"

    @pytest.mark.parametrize(
        "key,expected",
        [
            ("name", "volto"),
            ("title", "Plone Site (Volto)"),
            ("package_name", "plone.volto"),
            ("package_version", "5.0.4"),
        ],
    )
    def test_distribution_info(self, key, expected):
        result = dist_utils.distribution_info()
        assert isinstance(result, dict)
        assert result[key] == expected
