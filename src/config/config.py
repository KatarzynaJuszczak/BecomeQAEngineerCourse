import os
from typing import Any
from src.providers.os_provider import OSProvider
from src.providers.json_provider import JSONProvider


class Config:
    """Config class is responsible for storing framework's and env's configuration."""

    def __init__(self, config_providers) -> None:
        self.config_providers = config_providers

        self.conf_dict = {}
        self._register_list(
            [
                "USER_ROLE",
                "USERNAME",
                "BROWSER",
                "BASE_DIRECTORY"
            ]
        )

    def __getattr__(self, item_name: str) -> Any:
        """
        Magic method to get the value of item_name.
        If item_name doesn't exist it will raise an error.
        """

        if item_name not in self.conf_dict:
            raise AttributeError(f"Please register '{item_name}' var before usage")
        return self.conf_dict[item_name]

    def _register(self, item_name: str) -> None:
        """
        Internal function which retrieves the value of item_name parameter from the
        config providers and stores it in Config class for later usage.
        """

        for provider in self.config_providers:
            item_value = provider.get(item_name)
            if item_value != "item does not exist":
                self.conf_dict[item_name] = item_value
                return
        raise ValueError(f"{item_name} name is missing in config providers.")

    def _register_list(self, item_list: list) -> None:
        """Internal function that calls _register() for parameters list."""

        for item in item_list:
            self._register(item)


config = Config(
    [
        OSProvider(),
        JSONProvider(os.path.join(os.path.dirname(os.path.abspath(__file__)), "envs", "qa.json"))
    ]
)
