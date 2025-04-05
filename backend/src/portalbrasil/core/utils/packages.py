import pkg_resources


def package_version(package_name: str) -> str:
    """Return the version of an installed package."""
    package_dist = pkg_resources.get_distribution(package_name)
    return package_dist.version
