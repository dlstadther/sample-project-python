# Sample Project - Python

![Docs](https://github.com/dlstadther/sample-project-python/actions/workflows/docs.yml/badge.svg)
![Test](https://github.com/dlstadther/sample-project-python/actions/workflows/tests.yml/badge.svg)

Sample structure and setup for a Python project which includes:

* prek hooks (static formatters and type checking)
* mkdoc generation from docstrings
* unittest execution

## Installation

```shell
# install requirements
make init
make install

# install prek configuration
poetry run prek install
```


## Usage

### Run Prek Hooks

```shell
# To run the prek hooks against staged files before committing:
uv run prek run

# To run a particular prek hook against staged files before committing:
# uv run prek run <hook>
uv run prek run ruff-format
uv run prek run ruff
uv run prek run ty

# To run a particular prek hook against all files (staged and unstaged, before committing):
uv run prek run ruff --all-files

# run checks regardless of git status
uv run ruff format --check src
uv run ty src
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

```shell
# Build sdist and wheel
make build

# Only build wheel
uv build --wheel

# Test semantic release (dry-run, shows what would be released)
make release-dry-run

# Publish to PyPI
export UV_PUBLISH_TOKEN="<my-pypi-token>"
uv publish
uv publish --token "<my-pypi-token>"
```

## Prek Hooks

Prek hooks run during `git commit ...` in order to apply checks for quality and format prior to commit.

The checks contained in this repo include (in the order in which they run):
* Various checkers and formatters to verify valid file types, file size, and end of line and end of file whitespace/newlines
* `ruff format` applies standard code style formatting (just like `black`, but faster)
* `ruff` checks code for "lint"
* `ty` is used for static type checking
* `sqlfluff` checks and fixes sql formatting and linting
* `uv` checks on valid and aligned pyproject.toml and uv.lock files
* `commitlint` enforces commit message conforms to [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) format

If you want `ruff format` to ignore a particular section of code, you can add the comments `# fmt: off` and `# fmt: on` before and after the respective block of code (same as you would if using `black`).
* https://stackoverflow.com/a/58584557

If you want `ty` to ignore a particular line of code, you can add the comment `# type: ignore` to the end of that line.
If `# type: ignore` is added to the very top of a file, `ty` will ignore the entire file.

If you absolutely must commit without adhering to the prek hooks, then you can use `git commit -n ...` where `-n` is shorthand for `--no-verify`.

# TODOs
* [ ]
