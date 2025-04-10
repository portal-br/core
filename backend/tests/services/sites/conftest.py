from plone.restapi.testing import RelativeSession

import pytest


@pytest.fixture()
def app(functional):
    yield functional["app"]


@pytest.fixture()
def request_api_factory(app):
    def factory():
        url = app.absolute_url()
        api_session = RelativeSession(url)
        api_session.headers.update({"Accept": "application/json"})
        return api_session

    return factory
