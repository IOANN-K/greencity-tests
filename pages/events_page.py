from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.components.event_card_components import EventCardComponent

class EventsPage(BasePage):
    ITEMS_COUNT = (By.CSS_SELECTOR, ".items-found")
    EVENT_CARDS = (By.CSS_SELECTOR, "mat-card")

    def get_items_count(self):
        text = self.wait.until(By.CSS_SELECTOR, self.ITEMS_COUNT).text
        # Витягуємо число (наприклад, "31 items found")
        return int(''.join(filter(str.isdigit, text)))

    def get_cards(self):
        elements = self.driver.find_elements(*self.EVENT_CARDS)
        return [EventCardComponent(el) for el in elements]

    def navigate_to_eco_news(self):
        self.driver.find_element(*self.ECO_NEWS_LINK).click()