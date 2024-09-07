import os

from dotenv import load_dotenv

from python_template.logging import get_logger

logger = get_logger(__name__)

# load the environment variables
load_dotenv(override=True)


def vulture_ignore(obj):
    """Decorator to ignore vulture warnings for a function."""
    return obj


def get_env_variable(name: str) -> str:
    """Get an environment variable or raise an exception if it is not set.

    Args:
        name (str): name of the environment variable

    Raises:
        ValueError: variable is not set

    Returns:
        str: the environment variable value
    """
    value = os.getenv(name)

    if value is None:
        raise ValueError(f"Environment variable {name} is not set.")
    else:
        len_value = len(value)

        if len_value > 10:
            show_n_chars = 5
        elif len_value > 5:
            show_n_chars = 1
        else:
            show_n_chars = 0

        printed_value = value[:show_n_chars] + "*" * (len_value - show_n_chars)

        logger.debug(f"Environment variable {name} has value {printed_value}")
    return value


def set_project_name(name: str) -> None:
    """
    Set the project name for the files and in the file content to not manually change from the template.
    """

    mapping = {"python-template": name, "python_template": name.replace("-", "_")}

    for root, _, files in os.walk("."):
        # skip all hidden directories
        if "/." in root:
            continue

        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "r", errors="ignore") as f:
                content = f.read()

            for old, new in mapping.items():
                content = content.replace(old, new)

            with open(file_path, "w") as f:
                f.write(content)

            # move the file to the new name
            # TODO: Fix this
            # new_file_path = file_path
            # for old, new in mapping.items():
            #     new_file_path = new_file_path.replace(old, new)

            # if os.path.exists(new_file_path):
            #     os.rename(file_path, new_file_path)
