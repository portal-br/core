from portalbrasil.core.testing import ACCEPTANCE_TESTING
from portalbrasil.core.testing import FUNCTIONAL_TESTING
from portalbrasil.core.testing import INTEGRATION_TESTING
from pytest_plone import fixtures_factory
from zope.component.hooks import site

import pytest


pytest_plugins = ["pytest_plone"]


globals().update(
    fixtures_factory((
        (ACCEPTANCE_TESTING, "acceptance"),
        (FUNCTIONAL_TESTING, "functional"),
        (INTEGRATION_TESTING, "integration"),
    ))
)


@pytest.fixture(scope="class")
def portal_class(integration_class):
    if hasattr(integration_class, "testSetUp"):
        integration_class.testSetUp()
    portal = integration_class["portal"]
    with site(portal):
        yield portal
    if hasattr(integration_class, "testTearDown"):
        integration_class.testTearDown()
