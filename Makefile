TEST_DIR="tests"

# Build
build:
	uvx --from build pyproject-build --installer uv

# Clean
clean:
	rm -rf .nox/
	rm -rf .venv/
	rm -rf dist/
	rm -rf site/
	rm -f .coverage*

# Docs
doc-build:
	uv run mkdocs build

doc-serve: doc-build
	uv run mkdocs serve

doc-deploy:
	uv run mkdocs gh-deploy --force

# Setup
init: init-uv init-python

init-uv:
	curl -LsSf https://astral.sh/uv/$(shell cat .uv-version)/install.sh | sh

init-python:
	uv python install $(cat .python-version)

install:
	uv sync

lock:
	uv lock

# Validations
format:
	uv run ruff format --check .

lint: lint-python lint-sql

lint-python:
	uv run ruff check --output-format=github .

lint-sql:
	uv run sqlfluff lint .

type:
	uv run mypy .

test:
	uv run coverage run -m pytest -vv $(TEST_DIR) && uv run coverage report -m

test-all:
	uv run nox --reuse-venv=yes --no-install
