import nox


def _install_poetry(session: nox.Session) -> nox.Session:
    session.install("poetry")
    session.run("poetry", "install")
    return session


@nox.session(python=["3.9"])
def tests(session: nox.Session) -> None:
    session = _install_poetry(session=session)
    session.run("coverage", "run", "-m", "pytest")
    session.run("coverage", "report")


@nox.session
def lint(session: nox.Session) -> None:
    session = _install_poetry(session=session)
    session.run("black", "--check", ".")
    session.run("ruff", ".")


@nox.session
def typing(session: nox.Session) -> None:
    session = _install_poetry(session=session)
    session.run("mypy", ".")
