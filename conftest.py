import pytest
from src.applications.github.api.github_api import GitHubAPIClient
from src.applications.github.ui.github_ui import GitHubUILoginPage
from src.providers.browser_provider import BrowserProvider
from src.config.config import config


@pytest.fixture(scope="session")
def github_api_app():
    """Returns an instance of the GitHubAPIClient class."""

    github_api_client = GitHubAPIClient()

    yield github_api_client


@pytest.fixture(scope="session")
def github_login_page_object():
    """
    Opens Github login page.
    Returns an instance of the GitHubUILoginPage class.
    Closes browser.
    """

    driver = BrowserProvider.get_driver(config.BROWSER)
    timeout = config.TIMEOUT

    github_login_page = GitHubUILoginPage(driver, timeout)
    github_login_page.navigate_to_github_login_page()

    yield github_login_page

    github_login_page.close_browser()
