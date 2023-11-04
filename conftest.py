import pytest
from src.applications.github.api.github_api import GitHubAPIClient


@pytest.fixture(scope="session")
def github_api_app():
    """Returns an instance of the GitHubAPIClient class."""

    github_api_client = GitHubAPIClient()

    yield github_api_client
