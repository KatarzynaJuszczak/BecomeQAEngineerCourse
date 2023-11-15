from selenium import webdriver
from src.logger.logger import AFLogger

logger = AFLogger.get_logger("browser_provider")


class BrowserProvider:
    """Returns the initialized driver for desired browser."""

    @staticmethod
    def get_driver(browser_name):
        if browser_name == "ff":
            driver = webdriver.Firefox()
        elif browser_name == "chrome":
            driver = webdriver.Chrome()
        elif browser_name == "ff_remote":
            options = webdriver.FirefoxOptions()
            driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
                                      options=options)
        elif browser_name == "chrome_remote":
            options = webdriver.ChromeOptions()
            driver = webdriver.Remote(command_executor="http://localhost:4444/wd/hub",
                                      options=options)
        else:
            logger.error(f"Not supported browser {browser_name} was selected.")
            raise ValueError(f"Not supported browser {browser_name} was selected.")

        logger.debug(f"Selected browser: {driver.name}.")

        return driver
