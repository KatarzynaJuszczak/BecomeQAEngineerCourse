import pytest
from src.applications.github.api.github_api import GitHubAPIClient


@pytest.fixture
def github_api_client():
    """Returns an instance of the GitHubAPIClient class."""
    github_api_client = GitHubAPIClient()
    return github_api_client

