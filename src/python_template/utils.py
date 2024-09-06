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
