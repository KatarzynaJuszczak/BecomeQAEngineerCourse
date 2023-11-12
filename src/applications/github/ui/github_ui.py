from src.logger.logger import AFLogger
from selenium.webdriver.common.by import By
from src.applications.github.test_data import test_data
from src.applications.github.ui.base_page import BasePage

logger = AFLogger.get_logger("github ui")


class GitHubUILoginPage(BasePage):
    """Current class contains every UI usage we use in tests."""

    def __init__(self, driver, timeout):
        super().__init__(driver, timeout)

    def navigate_to_github_login_page(self):
        """Navigate to github login web page."""

        github_login_url = test_data.GITHUB_URL + test_data.LOGIN_PAGE_URL
        self.navigate_to_page(github_login_url)

    def try_to_login(self, username, password):
        """Try to log in into github with username and password."""

        self.input_text_into_element(By.ID, "login_field", username)
        self.input_text_into_element(By.ID, "password", password)
        self.click_element(By.NAME, "commit")

    def check_error_message(self):
        """Check error message on github login page."""

        error_msg = self.get_text_from_element(By.CLASS_NAME, "js-flash-alert")

        return error_msg
