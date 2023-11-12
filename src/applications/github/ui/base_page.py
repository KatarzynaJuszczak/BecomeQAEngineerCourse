from src.logger.logger import AFLogger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

logger = AFLogger.get_logger("base_page")


class BasePage:

    def __init__(self, driver, timeout):
        self.driver = driver
        self.timeout = timeout

    def navigate_to_page(self, page_url):
        """Navigate to a specific web page by page URL."""

        try:
            self.driver.get(page_url)
            logger.info(f"Navigated to page: {page_url}.")
        except Exception as e:
            logger.error(f"Error navigating to page: {e}.")
            raise e

    def find_el(self, by, locator_value):
        """Find a web element using the specified locator strategy and locator value."""

        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.presence_of_element_located((by, locator_value))
            )
            element = self.driver.find_element(by, locator_value)
            logger.info(f"Found element: {element}.")
            return element
        except TimeoutError:
            logger.error(f"Timed out waiting for element {by}: {locator_value}.")
            raise Exception(f"Timed out waiting for element {by}: {locator_value}.")
        except NoSuchElementException as e:
            logger.error(f"Element not found {by}: {locator_value}.")
            raise e

    def click_element(self, by, locator_value):
        """
        Click a web element identified by the specified locator strategy
        and locator value.
        """

        try:
            element = self.find_el(by, locator_value)
            element.click()
            logger.info(f"Clicked element {by}: {locator_value}.")
        except Exception as e:
            logger.error(f"Error {e} occurred when clicking element {by}: "
                         f"{locator_value}.")
            raise e

    def input_text_into_element(self, by, locator_value, text):
        """
        Input text into a text field identified by the specified locator strategy
        and locator value.
        """

        try:
            element = self.find_el(by, locator_value)
            element.send_keys(text)
            logger.info(f"Text '{text}' has been entered into element {by}: {locator_value}.")
        except Exception as e:
            logger.error(f"Error {e} occurred when entering text into element {by}: "
                         f"{locator_value}.")
            raise e

    def get_text_from_element(self, by, locator_value):
        """
        Get the text from a web element identified by the specified locator strategy
        and locator value.
        """

        try:
            element = self.find_el(by, locator_value)
            text = element.text
            logger.info(f"Text '{text}' has been read from element {by}: {locator_value}.")
            return text
        except Exception as e:
            logger.error(f"Error {e} occurred when reading text from element {by}: "
                         f"{locator_value}.")
            raise e

    def close_browser(self):
        """Close browser."""
        try:
            logger.info(f"Close browser: {self.driver.name}.")
            self.driver.quit()
        except Exception as e:
            logger.error(f"Error {e} occurred closing browser {self.driver.name}.")
            raise e
