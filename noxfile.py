import nox


def _install_package_manager(session: nox.Session) -> nox.Session:
    session.install("uv")
    session.run("make", "install")
    return session


@nox.session(python=["3.9", "3.10", "3.11", "3.12"])
def tests(session: nox.Session) -> None:
    session = _install_package_manager(session=session)
    pytest_posargs = session.posargs or ["-m", "not df"]
    session.run("uv", "run", "pytest", "-vv", *pytest_posargs)


@nox.session
def tests_extra_pandas(session: nox.Session) -> None:
    session = _install_package_manager(session=session)
    session.run("uv", "sync", "--extra", "df")
    session.run("uv", "run", "pytest", "-vv", "-m", "df")


@nox.session
def lint(session: nox.Session) -> None:
    session = _install_package_manager(session=session)
    session.run("make", "format")
    session.run("make", "lint")


@nox.session
def typing(session: nox.Session) -> None:
    session = _install_package_manager(session=session)
    session.run("make", "type")


@nox.session
def build(session: nox.Session) -> None:
    session = _install_package_manager(session=session)
    session.run("make", "build")
