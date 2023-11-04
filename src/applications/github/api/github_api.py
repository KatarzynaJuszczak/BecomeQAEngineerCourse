import requests
from src.logger.logger import AutomationFrameworkLogger
from src.config.config import Config, JSONConfigProvider

TestApiLogger = AutomationFrameworkLogger.get_logger("api_tests")
config = Config(config_providers=[JSONConfigProvider(env_type="github_api")])


class GitHubAPIClient:
    """Current class contains every API call we use in tests."""

    def __init__(self) -> None:
        pass

    def search_user(self, user_name):
        search_user_url = config.URLS["GITHUB_API_URL"] + config.URLS["SEARCH_USERS_URL"]
        TestApiLogger.info(f"Sending request to url: {search_user_url}")

        r = requests.get(f"{search_user_url}", params={'q': user_name})
        body = r.json()

        TestApiLogger.info(f"Response retrieved {body}")

        return body

    def search_repos(self, repo_name):
        search_repos_url = config.URLS["GITHUB_API_URL"] + config.URLS["SEARCH_REPOS_URL"]
        TestApiLogger.info(f"Sending request to url: {search_repos_url}")

        r = requests.get(f"{search_repos_url}", params={'q': repo_name})
        body = r.json()

        TestApiLogger.info(f"Response retrieved {body}")

        return body

    def search_commits(self, commit_hash):
        search_commits_url = config.URLS["GITHUB_API_URL"] + config.URLS["SEARCH_COMMITS_URL"]
        TestApiLogger.info(f"Sending request to url: {search_commits_url}")

        r = requests.get(f"{search_commits_url}", params={'q': commit_hash})
        body = r.json()

        TestApiLogger.info(f"Response retrieved {body}")
        return body
