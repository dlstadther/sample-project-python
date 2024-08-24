import nox


def _install_package_manager(session: nox.Session) -> nox.Session:
    session.install("uv")
    session.run("uv", "sync")
    return session


@nox.session
def tests(session: nox.Session) -> None:
    session = _install_package_manager(session=session)
    session.run("coverage", "run", "-m", "pytest", "-vv")
    session.run("coverage", "report")


@nox.session
def lint(session: nox.Session) -> None:
    session = _install_package_manager(session=session)
    session.run("ruff", "format", "--check", ".")
    session.run("ruff", "check", "--output-format=github", ".")
    session.run("sqlfluff", "lint", ".")


@nox.session
def typing(session: nox.Session) -> None:
    session = _install_package_manager(session=session)
    session.run("mypy", ".")
