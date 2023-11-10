from src.logger.logger import AFLogger
from selenium.webdriver.common.by import By
from src.applications.github.test_data import test_data
from src.applications.github.ui.base_page import BasePage

logger = AFLogger.get_logger("github ui")


class GitHubUILoginPage(BasePage):
    """Current class contains every UI usage we use in tests."""

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_github_login_page(self):
        github_login_url = test_data.GITHUB_URL + test_data.LOGIN_PAGE_URL
        self.navigate_to_page(github_login_url)

    def try_to_login(self, username, password):
        login_element = self.find_el(By.ID, "login_field")
        login_element.send_keys(username)

        password_element = self.find_el(By.ID, "password")
        password_element.send_keys(password)

        sign_in_button = self.find_el(By.NAME, "commit")
        sign_in_button.click()

    def check_error_message(self):
        error_msg = self.find_el(By.CLASS_NAME, "js-flash-alert")

        return error_msg
