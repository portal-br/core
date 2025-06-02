from dataclasses import dataclass
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


@dataclass
class CurrentVersions:
    base: str
    dependencies: str
    package: str


@pytest.fixture(scope="session")
def current_versions() -> CurrentVersions:
    from portalbrasil.core import __version__

    return CurrentVersions(
        base="1001",
        dependencies="1000",
        package=__version__,
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
