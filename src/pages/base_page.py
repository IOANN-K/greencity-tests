from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    """Base class for all Page Objects."""

    BASE_URL = "https://www.greencity.cx.ua/#"
    DEFAULT_TIMEOUT = 10

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    def open(self, path: str = ""):
        self.driver.get(f"{self.BASE_URL}{path}")
        return self

    def find(self, locator: tuple):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_all(self, locator: tuple):
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def click(self, locator: tuple):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return self

    def is_visible(self, locator: tuple) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except Exception:
            return False

    def get_text(self, locator: tuple) -> str:
        return self.find(locator).text
