import json
import os
from typing import Any


class OSConfigProvider:
    """OSConfigProvider class provides system environment variables."""

    @staticmethod
    def get(item_name: str) -> Any:
        """Get the value from the system environment variables by variable name."""

        env_value = os.getenv(item_name)
        return env_value


class JSONConfigProvider:
    """JSONConfigProvider class provides json config variables."""

    def __init__(self, env_type) -> None:
        self.env_type = env_type
        self.config_path = self._check_config_path()
        self.json_object = self._read_config(self.config_path)

    def _check_config_path(self):
        """Internal function which returns the path to the json file
        depending on the environment type."""

        module_path = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(module_path, "envs", f"{self.env_type.lower()}.json")
        if os.path.exists(config_path):
            return config_path
        else:
            raise AttributeError(f"Wrong env_type {self.env_type} was used.")

    @staticmethod
    def _read_config(config_path):
        """Internal function which opens json file and deserialize it
        to a Python object."""

        with open(config_path) as json_file:
            return json.load(json_file)

    def get(self, item_name: str) -> Any:
        """Get the value from the json file by parameter name"""

        json_value = self.json_object.get(item_name)
        return json_value


class Config:
    """Config class is responsible for storing framework's and env's configuration"""

    def __init__(self, config_providers) -> None:
        self.config_providers = config_providers  # STORE THE ORDER OF PROVIDERS
        self.conf_dict = {}  # STORE THE VALUES OF YOUR PARAMETERS

        # REGISTER PARAMETERS BEFORE USE
        self._register_list(
            [
                "URLS",
                "VALID_DATA",
                "NON_VALID_DATA"
            ]
        )

    def __getattr__(self, item_name: str) -> Any:
        """Magic method to get the value of item_name.
        If item_name doesn't exist it will raise an error."""

        if item_name not in self.conf_dict:
            raise AttributeError(f"Please register '{item_name}' var before usage")
        return self.conf_dict[item_name]

    def _register(self, item_name: str) -> None:
        """Internal function which retrieves the value of item_name parameter from the
        config providers and stores it in Config class for later usage."""

        for provider in self.config_providers:
            item_value = provider.get(item_name)
            if item_value is not None:
                self.conf_dict[item_name] = item_value
                return
        raise ValueError(f"{item_name} name is missing in config providers")

    def _register_list(self, item_list: list) -> None:
        """Internal function that calls _register() for parameters list."""

        for item in item_list:
            self._register(item)
