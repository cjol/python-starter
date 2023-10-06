# cls_finance

To bootstrap a new project, clone this project and do a global find-and-replace
for `cls_finance` and replace it with your project name.

## Setup

```bash
# Install dependencies
poetry install
```

## Running the project

```bash
# typecheck
poetry run pyright

# lint
poetry run black --check .
poetry run isort --check .

# Run the dev entry point
poetry run dev

# or, more fully:
poetry run python -m cls_finance

# run the tests without coverage
poetry run pytest

# Run the tests and display coverage
poetry run coverage run -m pytest
poetry run coverage report --skip-empty -m
```
