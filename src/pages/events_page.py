import allure
from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.components.header import Header
from src.components.filter_panel import FilterPanel
from src.components.event_card import EventCard


class EventsPage(BasePage):
    """Page Object for the GreenCity Events page."""

    PATH = "/events"

    PAGE_TITLE = (By.CSS_SELECTOR, "h1.events-title, .events-header h1")
    CREATE_EVENT_BTN = (By.CSS_SELECTOR, ".create-event-btn, button[aria-label='create-event']")
    PAGINATION = (By.CSS_SELECTOR, ".pagination, app-pagination")
    NO_RESULTS_MSG = (By.CSS_SELECTOR, ".no-events-message, .empty-state")
    LOADER = (By.CSS_SELECTOR, ".loader, .loading-spinner")

    def __init__(self, driver):
        super().__init__(driver)
        self.header = Header(driver)
        self.filter_panel = FilterPanel(driver)
        self.event_card = EventCard(driver)

    @allure.step("Open Events page")
    def open_events(self):
        self.open(self.PATH)
        return self

    @allure.step("Get page title text")
    def get_page_title(self) -> str:
        return self.get_text(self.PAGE_TITLE)

    @allure.step("Check if events list is loaded")
    def is_events_list_loaded(self) -> bool:
        return self.is_visible(self.event_card.CARDS_CONTAINER)

    @allure.step("Get total number of event cards")
    def get_events_count(self) -> int:
        return self.event_card.get_cards_count()

    @allure.step("Get all event titles")
    def get_event_titles(self) -> list[str]:
        return self.event_card.get_card_titles()

    @allure.step("Filter events by tag: {tag_text}")
    def filter_by_tag(self, tag_text: str):
        self.filter_panel.click_tag(tag_text)
        return self

    @allure.step("Filter events by Online type")
    def filter_online_events(self):
        self.filter_panel.select_online_events()
        return self

    @allure.step("Filter events by Offline type")
    def filter_offline_events(self):
        self.filter_panel.select_offline_events()
        return self

    @allure.step("Click event card at index {index}")
    def open_event(self, index: int = 0):
        self.event_card.click_card(index)
        return self

    @allure.step("Check if pagination is visible")
    def is_pagination_visible(self) -> bool:
        return self.is_visible(self.PAGINATION)

    @allure.step("Check if no-results message is shown")
    def is_no_results_shown(self) -> bool:
        return self.is_visible(self.NO_RESULTS_MSG)
