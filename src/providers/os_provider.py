import os
from typing import Any


class OSProvider:
    """OSProvider class provides system environment variables."""

    @staticmethod
    def get(item_name: str) -> Any:
        """
        Get the value from the system environment variables by variable name.
        If item doesn't exist returns proper info.
        """

        env_value = os.getenv(item_name, "item does not exist")
        return env_value
