# Sample Project - Python

![Docs](https://github.com/dlstadther/sample-project-python/actions/workflows/docs.yml/badge.svg)
![Test](https://github.com/dlstadther/sample-project-python/actions/workflows/tests.yml/badge.svg)

Sample structure and setup for a Python project which includes:
* pre-commit hooks (static formatters and type checking)
* mkdoc generation from docstrings
* unittest execution


## Installation
```shell
# install poetry
curl -sSL https://install.python-poetry.org | python3 -
# update poetry
poetry self update

# ensure venv is created within project
poetry config virtualenvs.in-project true

# install project dependencies into venv
poetry install
# install pre-commit configuration
poetry run pre-commit install
```


## Usage

### Run Pre-Commmit Hooks
```shell
# To run the pre-commit hooks against staged files before committing:
poetry run pre-commit run

# To run a particular pre-commit hook against staged files before committing:
# poetry run pre-commit run <hook>
poetry run pre-commit run black
poetry run pre-commit run ruff
poetry run pre-commit run mypy

# To run a particular pre-commit hook against all files (staged and unstaged, before committing):
poetry run pre-commit run ruff --all-files

# run checks regardless of git status
poetry run black --check src
poetry run mypy src
poetry run ruff src
```

### Run Unittests
```shell
# Run all unittests
make test

# Run specific tests
poetry run pytest -vv tests/test_placeholder.py::test_Sample_init
```

### Run All Checks
```shell
# Run all tests, lints, and checks
make test-all

# run all nox lints
poetry run nox -R -s lint
```

### Build Docs

```shell
# Build docs
make doc-build
make doc-serve
```


## Distribution
```shell
# Build sdist and wheel
poetry build

# Only build wheel
poetry build --format wheel

# Publish to PYPI
# https://python-poetry.org/docs/repositories/#configuring-credentials
poetry config pypi-token.pypi <my-token>
poetry publish
```


# Pre-commit Hooks
Pre-Commit hooks run during `git commit ...` in order to apply checks for quality and format prior to commit.

The checks contained in this repo include (in the order in which they run):
* Various checkers and formatters to verify valid file types, file size, and end of line and end of file whitespace/newlines
* The `black` formatter will apply a standard code style format
* `ruff` checks code for "lint"
* `mypy` is used for static type checking
* `poetry` checks on valid and aligned pyproject.toml and poetry.lock files
* `sqlfluff` checks and fixes sql formatting and linting

If you want `black` to ignore a particular section of code, you can add the comments `# fmt: off` and `# fmt: on` before and after the respective block of code.
* https://stackoverflow.com/a/58584557

If you want `mypy` to ignore a particular line of code, you can add the comment `# type: ignore` to the end of that line.
If `# type: ignore` is added to the very top of a file, `mypy` will ignore the entire file.

If you absolutely must commit without adhering to the pre-commit hooks, then you can use `git commit -n ...` where `-n` is shorthand for `--no-verify`.


# TODOs
* [ ]
