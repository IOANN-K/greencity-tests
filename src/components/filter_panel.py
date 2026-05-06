from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from src.components.base_component import BaseComponent


class FilterPanel(BaseComponent):
    """Filter panel component for events page."""

    FILTER_TAGS_CONTAINER = (By.CSS_SELECTOR, ".tags-filter, .event-filter-tags")
    TAG_ITEM = (By.CSS_SELECTOR, ".filter-tag, .tag-item")
    ACTIVE_TAG = (By.CSS_SELECTOR, ".filter-tag.active, .tag-item.active")
    EVENT_TYPE_ONLINE = (By.XPATH, "//span[contains(text(),'Online')]")
    EVENT_TYPE_OFFLINE = (By.XPATH, "//span[contains(text(),'Offline')]")
    RESET_FILTERS_BTN = (By.CSS_SELECTOR, ".reset-filters-btn, button[aria-label='reset']")

    def get_all_tags(self) -> list:
        return self.find_all(self.TAG_ITEM)

    def click_tag(self, tag_text: str):
        tags = self.get_all_tags()
        for tag in tags:
            if tag_text.lower() in tag.text.lower():
                tag.click()
                return self
        raise ValueError(f"Tag '{tag_text}' not found in filter panel")

    def get_active_tags(self) -> list:
        return self.find_all(self.ACTIVE_TAG)

    def is_tag_active(self, tag_text: str) -> bool:
        active_tags = self.get_active_tags()
        return any(tag_text.lower() in t.text.lower() for t in active_tags)

    def select_online_events(self):
        self.click(self.EVENT_TYPE_ONLINE)
        return self

    def select_offline_events(self):
        self.click(self.EVENT_TYPE_OFFLINE)
        return self

    def reset_filters(self):
        self.click(self.RESET_FILTERS_BTN)
        return self
