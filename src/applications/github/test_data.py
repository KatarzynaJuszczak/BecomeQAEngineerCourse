import os
from typing import Any
from src.providers.json_provider import JSONProvider


class GithubTestData:
    """
    GithubTestData class is responsible for storing testing data for Github app
    from JSON file.
    """

    def __init__(self, test_data_path) -> None:
        self.test_data_path = test_data_path
        self.test_data_dict = {}
        self._register_list(
            [
                "GITHUB_API_URL",
                "GITHUB_URL",
                "SEARCH_USERS_URL",
                "SEARCH_REPOS_URL",
                "SEARCH_COMMITS_URL",
                "LOGIN_PAGE_URL",
                "VALID_USER_NAME",
                "VALID_REPO_NAME",
                "VALID_COMMIT_HASH"
            ]
        )

    def __getattr__(self, item_name: str) -> Any:
        """
        Magic method to get the value of item_name.
        If item_name doesn't exist it will raise an error.
        """

        if item_name not in self.test_data_dict:
            raise AttributeError(f"Please register '{item_name}' var before usage.")
        return self.test_data_dict[item_name]

    def _register(self, item_name: str) -> None:
        """
        Internal function which retrieves the value of item_name parameter from the
        JSON provider and stores it in GithubTestData class for later usage.
        """

        json_provider = JSONProvider(self.test_data_path)
        item_value = json_provider.get(item_name)
        if item_value != "item does not exist":
            self.test_data_dict[item_name] = item_value
        else:
            raise ValueError(f"{item_name} name is missing in test data file.")

    def _register_list(self, item_list: list) -> None:
        """Internal function that calls _register() for parameters list."""

        for item in item_list:
            self._register(item)


test_data_json_file = "github_test_data.json"

test_data_dir = os.path.dirname(os.path.abspath(__file__))
test_data_json_path = os.path.join(test_data_dir, "test_data", test_data_json_file)

test_data = GithubTestData(test_data_json_path)
