def sanitize_gs_version(version: str) -> str:
    # Instance version was not pkg_resources compatible...
    version = version.replace("devel (svn/unreleased)", "dev")
    version = version.rstrip("-final")
    version = version.rstrip("final")
    version = version.replace("alpha", "a")
    version = version.replace("beta", "b")
    version = version.replace("-", ".")
    return version
