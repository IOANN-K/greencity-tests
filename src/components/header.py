from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent


class Header(BaseComponent):
    """Header navigation component."""

    LOGO = (By.CSS_SELECTOR, ".header-logo")
    NAV_EVENTS = (By.CSS_SELECTOR, "a[href*='events']")
    USER_ICON = (By.CSS_SELECTOR, ".header-user-icon, .user-avatar")
    SIGN_IN_BTN = (By.CSS_SELECTOR, ".sign-in-btn, button[aria-label='sign-in']")
    LANGUAGE_TOGGLE = (By.CSS_SELECTOR, ".language-toggle, .lang-switch")

    def click_events(self):
        self.click(self.NAV_EVENTS)
        return self

    def is_logo_visible(self) -> bool:
        return self.is_visible(self.LOGO)

    def click_sign_in(self):
        self.click(self.SIGN_IN_BTN)
        return self
