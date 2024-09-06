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
        logger.debug(f"Environment variable {name} has value {value[:min(10, len(value))]}")
    return value
