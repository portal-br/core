import pytest


@pytest.fixture(scope="class")
def portal(portal_class):
    yield portal_class


class TestSystemGet:
    @pytest.fixture(autouse=True)
    def _setup(self, api_manager_request):
        self.api_session = api_manager_request

    def test_response_type(self):
        response = self.api_session.get("/@system")
        data = response.json()
        assert isinstance(data, dict)

    @pytest.mark.parametrize(
        "key,type_",
        (
            ("@id", str),
            ("cmf_version", str),
            ("debug_mode", str),
            ("distribution", dict),
            ("pil_version", str),
            ("plone_restapi_version", str),
            ("plone_version", str),
            ("plone_volto_version", str),
            ("portalbrasil", dict),
            ("python_version", str),
            ("upgrade", bool),
        ),
    )
    def test_keys(self, key, type_):
        response = self.api_session.get("/@system")
        data = response.json()
        assert key in data
        assert isinstance(data[key], type_)

    @pytest.mark.parametrize(
        "key,expected",
        (
            ("cmf_version", "3.7"),
            ("debug_mode", "No"),
            ("plone_restapi_version", "9.13.3"),
            ("plone_version", "6.1.1"),
            ("upgrade", False),
        ),
    )
    def test_values(self, key, expected):
        response = self.api_session.get("/@system")
        data = response.json()
        assert data[key] == expected

    @pytest.mark.parametrize(
        "key,expected",
        (
            ("profile_version_file_system", "1000"),
            ("profile_version_installed", "1000"),
            ("version", "1.0.0a0"),
        ),
    )
    def test_portalbrasil(self, key, expected):
        response = self.api_session.get("/@system")
        data = response.json()
        assert data["portalbrasil"][key] == expected

    @pytest.mark.parametrize(
        "key,expected",
        (
            ("name", "volto"),
            ("package_name", "plone.volto"),
            ("title", "Plone Site (Volto)"),
        ),
    )
    def test_distribution(self, key, expected):
        response = self.api_session.get("/@system")
        data = response.json()
        assert data["distribution"][key] == expected
