.PHONY: sync check fix format check-format lint check-lint check-types test pre-commit
.PHONY: docs docs-build clean
sync:
	@$(call pinfo,Installing project with all dependencies)
	uv sync --all-groups

check: check-format check-lint check-types

fix: format lint

format:
	@$(call pinfo,[ruff] Formatting code...)
	uv run ruff format

check-format:
	@$(call pinfo,[ruff] Checking code format...)
	uv run ruff format --check

lint:
	@$(call pinfo,[ruff] Linting code...)
	uv run ruff check --fix

check-lint:
	@$(call pinfo,[ruff] Checking code linting...)
	uv run ruff check --show-fixes --unsafe-fixes

check-types:
	@$(call pinfo,[pyrefly] Checking code typings....)
	uv run pyrefly check

test:
	@$(call pinfo,Executing all the tests...)
	uv run pytest

pre-commit:
	@$(call pinfo,Setup pre-commit...)
	uv run pre-commit install

clean:
	@$(call pinfo,Cleaning up generated files...)
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".ruff_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "site" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".venv" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".direnv" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".web" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".state" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name ".coverage*" -delete 2>/dev/null || true
	find . -type f -name "coverage.xml" -delete 2>/dev/null || true
	find . -type f -name ".python-version" -delete 2>/dev/null || true
	@$(call pinfo,Cleanup complete!)
