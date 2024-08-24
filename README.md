# Sample Project - Python

![Docs](https://github.com/dlstadther/sample-project-python/actions/workflows/docs.yml/badge.svg)
![Test](https://github.com/dlstadther/sample-project-python/actions/workflows/tests.yml/badge.svg)

Sample structure and setup for a Python project which includes:
* pre-commit hooks (static formatters and type checking)
* mkdoc generation from docstrings
* unittest execution


## Installation
```shell
# install requirements
make init
make install

# install pre-commit configuration
poetry run pre-commit install
```


## Usage

### Run Pre-Commit Hooks
```shell
# To run the pre-commit hooks against staged files before committing:
uv run pre-commit run

# To run a particular pre-commit hook against staged files before committing:
# uv run pre-commit run <hook>
uv run pre-commit run ruff-format
uv run pre-commit run ruff
uv run pre-commit run mypy

# To run a particular pre-commit hook against all files (staged and unstaged, before committing):
uv run pre-commit run ruff --all-files

# run checks regardless of git status
uv run ruff format --check src
uv run mypy src
uv run ruff src
```

### Run Unittests
```shell
# Run all unittests
make test

# Run specific tests
uv run pytest -vv tests/test_placeholder.py::test_Sample_init
```

### Run All Checks
```shell
# Run all tests, lints, and checks
make test-all

# run all nox lints
uv run nox -R -s lint
```

### Build Docs

```shell
# Build docs
make doc-build
make doc-serve
```


## Distribution
> As of 2024-08-22, uv does not yet have dedicated commands for building and publishing a package.
> Their [documentation recommends](https://docs.astral.sh/uv/guides/publish/) using the PyPA tools `build` and `twine`.
```shell
# Build sdist and wheel
uvx --from build pyproject-build --installer uv

# Only build wheel
uvx --from build pyproject-build --installer uv --wheel

# Publish to TEST PyPI
export TWINE_USERNAME="__token__"
export TWINE_PASSWORD="<my-pypi-token>"
uvx twine upload --repository testpypi dist/*

# Publish to PyPI
uvx twine upload dist/*
```


# Pre-commit Hooks
Pre-Commit hooks run during `git commit ...` in order to apply checks for quality and format prior to commit.

The checks contained in this repo include (in the order in which they run):
* Various checkers and formatters to verify valid file types, file size, and end of line and end of file whitespace/newlines
* `ruff format` applies standard code style formatting (just like `black`, but faster)
* `ruff` checks code for "lint"
* `mypy` is used for static type checking
* `sqlfluff` checks and fixes sql formatting and linting
* (COMING SOON) `uv` checks on valid and aligned pyproject.toml and uv.lock files
* `commitlint` enforces commit message conforms to [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) format

If you want `ruff format` to ignore a particular section of code, you can add the comments `# fmt: off` and `# fmt: on` before and after the respective block of code (same as you would if using `black`).
* https://stackoverflow.com/a/58584557

If you want `mypy` to ignore a particular line of code, you can add the comment `# type: ignore` to the end of that line.
If `# type: ignore` is added to the very top of a file, `mypy` will ignore the entire file.

If you absolutely must commit without adhering to the pre-commit hooks, then you can use `git commit -n ...` where `-n` is shorthand for `--no-verify`.


# TODOs
* [ ]
