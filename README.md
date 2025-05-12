# Python Template
This is a template for a python project using `uv` as a package manager.

## uv
uv is an extremely fast Python package manager. Docs can be found [here](https://docs.astral.sh/uv/). It's a single tool to replace pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv, and more, with speeds 10-100x faster than pip.

### Installation
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Adding and removing dependencies
- Add a dependency: `uv add <package_name>`
- Add a development dependency: `uv add --dev <package_name>`
- Remove a dependency: `uv remove <package_name>`

### Managing the virtual environment
- Update the project's environment: `uv sync`
- Update the project's lockfile: `uv lock`
- Create a virtual environment: `uv venv`
- Display the project's dependency tree: `uv tree`

### Running commands
- Run a command or script: `uv run <command>`
- Run and install commands provided by Python packages: `uv tool <command>`

## Coverage
Check whether your code is properly tested: `coverage .`

## Vulture
Check whether your code is used: `vulture . [--min-confidence <int>]`

## Pylint 
Lint your code: `pylint .`

## Ruff
I actually use the following commands (with the alias `ru`):
- Formatting: `ruff format`
- Linting and fixing: `ruff check --fix`
