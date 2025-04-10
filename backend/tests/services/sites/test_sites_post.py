import pytest


@pytest.fixture()
def answers():
    return {
        "site_id": "portal",
        "title": "Plone",
        "description": "Plone Site",
        "default_language": "pt-br",
        "portal_timezone": "America/Sao_Paulo",
        "setup_content": True,
    }


class TestSitesPost:
    @pytest.fixture(autouse=True)
    def _setup(self, api_manager_request):
        self.api_session = api_manager_request

    def test_post(self, answers):
        distribution_name = "volto"
        response = self.api_session.post(f"@sites/{distribution_name}", json=answers)
        data = response.json()
        assert response.status_code == 200
        assert isinstance(data, dict)
        assert data["id"] == answers["site_id"]
        assert data["_profile_id"] == "portalbrasil.core:base"
