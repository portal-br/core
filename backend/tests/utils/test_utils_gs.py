from portalbrasil.core.utils import gs as gs_utils

import pytest


class TestUtilsGS:
    @pytest.mark.parametrize(
        "version,expected",
        [
            ("1.0.0-devel (svn/unreleased)", "1.0.0.dev"),
            ("1.0.0-final", "1.0.0"),
            ("1.0.0final", "1.0.0"),
            ("1.0.0alpha1", "1.0.0a1"),
            ("1.0.0beta1", "1.0.0b1"),
            ("1-0-0", "1.0.0"),
        ],
    )
    def test_sanitize_gs_version(self, version, expected):
        result = gs_utils.sanitize_gs_version(version)
        assert result == expected
