from src.logger.logger import AFLogger
from selenium import webdriver
from selenium.webdriver.common.by import By

logger = AFLogger.get_logger("github_ui")


class GitHubUILoginPage:
    """Current class contains every UI usage we use in tests."""

    def __init__(self):
        self.driver = webdriver.Firefox()

    def navigate_to_page(self):
        github_login_url = "https://github.com/login"
        self.driver.get(github_login_url)
        logger.info(f"Page {github_login_url} has been open.")

    def try_to_login(self, username, password):
        login_element = self.driver.find_element(By.ID, "login_field")
        login_element.send_keys(username)

        password_element = self.driver.find_element(By.ID, "password")
        password_element.send_keys(password)

        sign_in_button = self.driver.find_element(By.NAME, "commit")
        sign_in_button.click()

    def check_error_message(self):
        error_msg = self.driver.find_element(By.CLASS_NAME, "js-flash-alert")

        return error_msg

    def close_browser(self):
        self.driver.quit()
        logger.info(f"The browser {self.driver.name} has been closed.")
