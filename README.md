# python_starter

To bootstrap a new project, clone this project and do a global find-and-replace
for `python_starter` and replace it with your project name. Also rename the
`python_starter` directory to match.

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
poetry run python -m python_starter

# run the tests without coverage
poetry run pytest

# Run the tests and display coverage
poetry run coverage run -m pytest
poetry run coverage report --skip-empty -m
```
