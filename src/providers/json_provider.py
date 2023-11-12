import json
from typing import Any


class JSONProvider:
    """JSONProvider class provides JSON variables."""

    def __init__(self, json_path) -> None:
        self.json_path = json_path
        self.json_object = self._read_json()

    def _read_json(self):
        """
        Internal function which opens JSON file and deserialize it to a Python object.
        """

        try:
            with open(self.json_path) as json_file:
                json_object = json.load(json_file)
                return json_object
        except FileNotFoundError:
            raise Exception(f"JSON file {self.json_path} not found.")

    def get(self, item_name: str) -> Any:
        """
        Get the value from the JSON file by parameter name.
        If item doesn't exist returns proper info.
        """

        json_value = self.json_object.get(item_name, "item does not exist")
        return json_value
