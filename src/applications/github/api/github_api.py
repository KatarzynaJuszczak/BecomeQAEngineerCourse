import requests
from src.logger.logger import AFLogger
from src.applications.github.test_data import test_data

logger = AFLogger.get_logger("github_api")


class GitHubAPIClient:
    """Current class contains every API call we use in tests."""

    def search_user(self, user_name):
        """
        This function searches for github user using the username and retrieves the JSON
        encoded response with the user's data, if any.
        """

        search_user_url = test_data.GITHUB_API_URL + test_data.SEARCH_USERS_URL
        logger.info(f"Sending request to url: {search_user_url}")

        r = requests.get(f"{search_user_url}", params={'q': user_name})
        logger.info(f"Response: {r}")

        body = r.json()
        logger.debug(f"Response retrieved: {body}")

        return body

    def search_repos(self, repo_name):
        """
        This function searches for github repository using the repository name and
        retrieves the json encoded response with the repository data, if any.
        """

        search_repos_url = test_data.GITHUB_API_URL + test_data.SEARCH_REPOS_URL
        logger.info(f"Sending request to url: {search_repos_url}")

        r = requests.get(f"{search_repos_url}", params={'q': repo_name})
        logger.info(f"Response: {r}")

        body = r.json()
        logger.debug(f"Response retrieved {body}")

        return body

    def search_commits(self, commit_hash):
        """
        This function searches for specific commit using the commit hash and
        retrieves the json encoded response with the commit data, if any.
        """

        search_commits_url = test_data.GITHUB_API_URL + test_data.SEARCH_COMMITS_URL
        logger.info(f"Sending request to url: {search_commits_url}")

        r = requests.get(f"{search_commits_url}", params={'q': commit_hash})
        logger.info(f"Response: {r}")

        body = r.json()
        logger.debug(f"Response retrieved {body}")

        return body
