TEST_DIR="tests"

doc-build:
	poetry run mkdocs build

doc-serve: doc-build
	poetry run mkdocs serve

doc-deploy:
	poetry run mkdocs gh-deploy --force

test:
	poetry run coverage run -m pytest -vv $(TEST_DIR) && poetry run coverage report -m

test-all:
	poetry run nox -r
