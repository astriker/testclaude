# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build/Test Commands

- **Lint**: `ruff check .`
- **Type check**: `mypy src`
- **Run all tests**: `pytest`
- **Run tests with coverage**: `pytest --cov=src`
- **Run a single test file**: `pytest tests/test_calculator.py`
- **Run a single test**: `pytest tests/test_calculator.py::test_add`
- **Install dependencies**: `pip install -r requirements.txt`
- **Setup pre-commit hooks**: `pre-commit install`

## Architecture

This is a simple Python project with pytest for testing.

- `src/` - Main source code (importable as `src.module`)
- `tests/` - Test files using pytest (import from src using `from src.calculator import ...`)
