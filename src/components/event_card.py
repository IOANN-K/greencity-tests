from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from src.components.base_component import BaseComponent


class EventCard(BaseComponent):
    """Single event card component."""

    CARDS_CONTAINER = (By.CSS_SELECTOR, ".events-list, .event-cards-container")
    CARD = (By.CSS_SELECTOR, ".event-card, app-events-list-item")
    CARD_TITLE = (By.CSS_SELECTOR, ".event-title, .event-name")
    CARD_DATE = (By.CSS_SELECTOR, ".event-date, .event-time")
    CARD_TAGS = (By.CSS_SELECTOR, ".event-tags .tag, .event-card-tag")
    CARD_IMAGE = (By.CSS_SELECTOR, ".event-image img, .event-card-img")
    CARD_ORGANIZER = (By.CSS_SELECTOR, ".event-organizer, .organizer-name")

    def get_all_cards(self) -> list[WebElement]:
        return self.find_all(self.CARD)

    def get_cards_count(self) -> int:
        return len(self.get_all_cards())

    def get_card_titles(self) -> list[str]:
        cards = self.get_all_cards()
        titles = []
        for card in cards:
            try:
                title_el = card.find_element(By.CSS_SELECTOR, ".event-title, .event-name")
                titles.append(title_el.text)
            except Exception:
                pass
        return titles

    def click_card(self, index: int = 0):
        cards = self.get_all_cards()
        if index >= len(cards):
            raise IndexError(f"Card index {index} out of range (total: {len(cards)})")
        cards[index].click()
        return self

    def get_card_tags(self, card: WebElement) -> list[str]:
        try:
            tag_elements = card.find_elements(By.CSS_SELECTOR, ".event-tags .tag, .event-card-tag")
            return [t.text for t in tag_elements]
        except Exception:
            return []
