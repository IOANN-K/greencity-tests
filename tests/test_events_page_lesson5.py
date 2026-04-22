import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from utils import log_step, wait_element, wait_clickable, click_with_js, clear_and_type

BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"
SEARCH_INPUT = (By.CSS_SELECTOR, "input[placeholder*='Search']")
SEARCH_ICON  = (By.CSS_SELECTOR, "div.container-img")
EVENT_CARD   = (By.CLASS_NAME, "event-list-item")
EVENT_NAME   = (By.CLASS_NAME, "event-name")


class TestEventsPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        self.wait = WebDriverWait(self.driver, 15)
        log_step("SETUP", "Browser opened, navigated to events page")

    def tearDown(self):
        self.driver.quit()
        log_step("TEARDOWN", "Browser closed")

    def _open_search(self):
        icon = wait_clickable(self.driver, SEARCH_ICON)
        click_with_js(self.driver, icon)
        return wait_element(self.driver, SEARCH_INPUT)

    def _wait_results(self):
        self.wait.until(lambda d:
            d.find_elements(*EVENT_NAME) or
            d.find_elements(By.XPATH, "//*[contains(text(),'find any results') or contains(text(),'не знайшли')]")
        )

    # ====================== TESTS ======================

    def test_filter_by_type_social(self):
        """TC-EV-001: Filter events by type Social"""
        log_step("TC-EV-001", "Filter by type: Social")

        filter_btn = wait_clickable(self.driver,
            (By.XPATH, "//div[contains(@class,'filter-container')]//*[contains(text(),'Type')]"))
        filter_btn.click()

        social = wait_clickable(self.driver,
            (By.XPATH, "//span[contains(text(),'Social') or contains(text(),'Соціальний')]"))
        social.click()

        cards = self.driver.find_elements(By.TAG_NAME, "mat-card")
        log_step("TC-EV-001", f"Cards found: {len(cards)}")
        for card in cards:
            self.assertIn("SOCIAL", card.text.upper(), "Card without Social tag found")

        log_step("TC-EV-001", "PASSED")

    def test_search_by_name(self):
        """TC-EV-002: Search event by title 'Eco Meetup'"""
        log_step("TC-EV-002", "Search by title: Eco Meetup")

        search_field = self._open_search()
        clear_and_type(search_field, "Eco Meetup")
        search_field.send_keys(Keys.ENTER)

        self._wait_results()

        results = self.driver.find_elements(*EVENT_NAME)
        log_step("TC-EV-002", f"Results found: {len(results)}")
        self.assertGreater(len(results), 0, "TC-EV-002 FAIL: No search results appeared")

        log_step("TC-EV-002", "PASSED")

    def test_filter_by_date_range(self):
        """TC-EV-003: Filter events by today's date"""
        log_step("TC-EV-003", "Filter by date range")

        date_filter = wait_clickable(self.driver,
            (By.XPATH, "//*[contains(text(),'Date')]"))
        date_filter.click()

        today = wait_clickable(self.driver, (By.CSS_SELECTOR, ".mat-calendar-body-today"))
        today.click()

        results = self.driver.find_elements(*EVENT_CARD)
        log_step("TC-EV-003", f"Events found for selected date: {len(results)}")

        log_step("TC-EV-003", "PASSED")

    def test_unauthorized_creation_negative(self):
        """TC-EV-004 [Negative]: Unauthorized event creation should be blocked"""
        log_step("TC-EV-004", "Attempt to create event without login")

        create_btn = wait_clickable(self.driver, (By.CSS_SELECTOR, "div.create button"))
        try:
            create_btn.click()
        except Exception:
            click_with_js(self.driver, create_btn)

        auth_modal_locator = (By.CSS_SELECTOR, "app-auth-modal, .modal-container")
        try:
            auth_modal = wait_element(self.driver, auth_modal_locator, timeout=5)
            is_displayed = auth_modal.is_displayed()
        except Exception:
            is_displayed = False

        log_step("TC-EV-004", f"Auth modal visible: {is_displayed}")
        self.assertTrue(is_displayed, "TC-EV-004 FAIL: Auth modal did not appear")

        log_step("TC-EV-004", "PASSED")

    def test_non_existent_search_negative(self):
        """TC-EV-005 [Negative]: Search for non-existent event shows empty state"""
        log_step("TC-EV-005", "Search for non-existent event")

        search_field = self._open_search()
        clear_and_type(search_field, "NonExistentEvent12345")
        search_field.send_keys(Keys.ENTER)

        no_results = wait_element(self.driver,
            (By.XPATH, "//*[contains(text(),'find any results') or contains(text(),'не знайшли')]"))
        self.assertTrue(no_results.is_displayed(), "TC-EV-005 FAIL: Empty-state message not shown")

        log_step("TC-EV-005", "PASSED")

    def test_parameterized_search(self):
        """TC-EV-006: Search with multiple terms, each should return results"""
        log_step("TC-EV-006", "Parameterized search")

        search_terms = ["E", "Eco", "Green"]
        search_field = self._open_search()

        for term in search_terms:
            with self.subTest(term=term):
                clear_and_type(search_field, term)
                search_field.send_keys(Keys.ENTER)
                self._wait_results()

                results = self.driver.find_elements(*EVENT_NAME)
                log_step("TC-EV-006", f"Term '{term}': {len(results)} results")
                self.assertGreater(len(results), 0, f"TC-EV-006 FAIL: No results for term '{term}'")

        log_step("TC-EV-006", "PASSED")


if __name__ == "__main__":
    unittest.main(verbosity=2)