# Python Template
This is a template for a python project using `rye` as a package manager.

## Rye
Rye is a comprehensive project and package management solution for Python. Important commands are
- Add a dependency: `rye add [--dev] <package_name>`
- Sync virtual environment: `rye sync`

## Coverage
Check whether your code is properly tested: `coverage .`

## Vulture
Check whether your code is used: `vulture . [--min-confidence <int>]`

## Pylint 
Lint your code: `pylint .`

## Ruff
I acutally don't know if this is much different from `rye fmt`and `rye lint, but I usually use (with an alias):
- Formatting: `ruff format`
- Linting and fixing: `ruff check --fix`
