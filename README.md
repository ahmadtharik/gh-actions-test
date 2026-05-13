# gh-actions

A simple Python project to test GitHub Actions CI/CD workflows.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run Tests

```bash
pytest tests/ -v
```

## GitHub Actions

Tests run automatically on push and pull requests to `main`, across Python 3.10, 3.11, and 3.12.
