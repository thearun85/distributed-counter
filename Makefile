.PHONY: lint fmt typecheck test all clean

lint:
	poetry run ruff check counter tests

fmt:
	poetry run ruff format counter tests
	poetry run ruff check --fix counter tests

typecheck:
	poetry run mypy counter tests

test:
	poetry run pytest -v -s

all: fmt lint typecheck test

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .mypy_cache -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
