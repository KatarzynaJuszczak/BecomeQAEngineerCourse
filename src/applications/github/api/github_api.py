import requests
from src.logger.logger import AFLogger
from src.applications.github.test_data import test_data

logger = AFLogger.get_logger("github_api")


class GitHubAPIClient:
    """Current class contains every API call we use in tests."""

    def search_user(self, user_name):
        search_user_url = test_data.GITHUB_API_URL + test_data.SEARCH_USERS_URL
        logger.info(f"Sending request to url: {search_user_url}")

        r = requests.get(f"{search_user_url}", params={'q': user_name})
        logger.info(f"Response: {r}")

        body = r.json()
        logger.debug(f"Response retrieved: {body}")

        return body

    def search_repos(self, repo_name):
        search_repos_url = test_data.GITHUB_API_URL + test_data.SEARCH_REPOS_URL
        logger.info(f"Sending request to url: {search_repos_url}")

        r = requests.get(f"{search_repos_url}", params={'q': repo_name})
        logger.info(f"Response: {r}")

        body = r.json()
        logger.debug(f"Response retrieved {body}")

        return body

    def search_commits(self, commit_hash):
        search_commits_url = test_data.GITHUB_API_URL + test_data.SEARCH_COMMITS_URL
        logger.info(f"Sending request to url: {search_commits_url}")

        r = requests.get(f"{search_commits_url}", params={'q': commit_hash})
        logger.info(f"Response: {r}")

        body = r.json()
        logger.debug(f"Response retrieved {body}")

        return body
