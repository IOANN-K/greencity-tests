from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Локатори
    LANGUAGE_BUTTON = (By.CSS_SELECTOR, ".language-switcher")
    EVENTS_LINK = (By.XPATH, "//a[contains(@href, '/events')]")
    ECO_NEWS_LINK = (By.XPATH, "//a[contains(@href, '/news')]")

    def switch_language(self, lang: str):
        # Логіка кліку на перемикач мов
        self.wait.until(EC.element_to_be_clickable(self.LANGUAGE_BUTTON)).click()
        lang_option = (By.XPATH, f"//ul//li[contains(text(), '{lang.upper()}')]")
        self.wait.until(EC.element_to_be_clickable(lang_option)).click()

    def get_events_link(self):
        return self.wait.until(EC.visibility_of_element_to_be_clickable(self.EVENTS_LINK))

    def navigate_to_events(self):
        self.get_events_link().click()