from src.logger.logger import AFLogger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = AFLogger.get_logger("base_page")


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_el(self, locator_name, locator_value):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((locator_name, locator_value))
            )
            return self.driver.find_element(locator_name, locator_value)
        except TimeoutError:
            raise Exception(f"Element didn't found.")

    def navigate_to_page(self, page_url):
        logger.info(f"Navigate to page: {page_url}")
        self.driver.get(page_url)

    def close_browser(self):
        logger.info(f"Close browser: {self.driver.name}")
        self.driver.quit()
