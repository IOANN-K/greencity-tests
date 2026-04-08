import unittest
import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from utils import log_step, wait_clickable, wait_element, click_with_js, scroll_into_view, clear_and_type

BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"


class TestEventsPage(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()

        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        self.wait = WebDriverWait(self.driver, 15)

        log_step("TEST_SETUP", f"Navigated to {BASE_URL}")
        log_step("BROWSER_READY", "Window maximized")

    def tearDown(self):
        self.driver.quit()
        log_step("TEST_TEARDOWN", "Browser closed successfully")


    # ====================== TESTS ======================

    def test_filter_by_type(self):
        """TC-EV-001: Filter by Type (Social)"""
        log_step("TEST_START", "TC-EV-001 - Filter by Type (Social)")

        log_step("OPEN_TYPE_DROPDOWN")
        type_filter = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'dropdown') and .//mat-label[contains(., 'Type') or contains(., 'Тип')]]//mat-select")
        ))
        scroll_into_view(self.driver, type_filter)
        click_with_js(self.driver, type_filter)

        log_step("SELECT_SOCIAL_OPTION", "Selecting 'Social' / 'Соціальний'")
        social_option = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//mat-option[contains(., 'Social') or contains(., 'Соціальний')]")
        ))
        social_option.click()

        log_step("WAIT_FOR_RESULTS")
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "event-list-item")))

        events = self.driver.find_elements(By.CLASS_NAME, "event-list-item")
        log_step("RESULTS_COUNT", f"Found {len(events)} events after Social filter")

        for i, event in enumerate(events):
            card_tags = event.find_elements(By.CSS_SELECTOR, ".tag-active")
            tag_texts = [t.text.strip().upper() for t in card_tags]

            has_correct_tag = any(tag in ["SOCIAL", "СОЦІАЛЬНИЙ"] for tag in tag_texts)

            if not has_correct_tag:
                log_step("TAG_MISMATCH", f"Card {i+1}: Found tags {tag_texts}", "WARN")

            self.assertTrue(has_correct_tag,
                            f"TC-EV-001: Social tag missing in card {i+1}. Found: {tag_texts}")

        log_step("TEST_PASSED", "TC-EV-001 completed successfully")


    def test_search_by_title(self):
        """TC-EV-002: Search by Specific Title"""
        log_step("TEST_START", "TC-EV-002 - Search by Specific Title")

        search_query = "Eco Meetup"

        log_step("CLICK_SEARCH_ICON")
        click_with_js(self.driver,
            self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".container-img"))))

        log_step("ENTER_SEARCH_QUERY", f"'{search_query}'")
        search_input = wait_element(self.driver, (By.CSS_SELECTOR, "input[placeholder*='Search']"))
        clear_and_type(search_input, search_query + Keys.ENTER)

        log_step("WAIT_FOR_SEARCH_RESULTS")
        self.wait.until(lambda d: len(d.find_elements(By.CLASS_NAME, "event-name")) > 0 or
                                  len(d.find_elements(By.XPATH, "//*[contains(text(), 'find any results') or contains(text(), 'не знайшли')]")) > 0)

        count = len(self.driver.find_elements(By.CLASS_NAME, "event-name"))
        log_step("RESULTS_FOUND", f"Found {count} results for '{search_query}'")

        self.assertGreater(count, 0,
                           f"TC-EV-002: No results found for '{search_query}'")

        log_step("TEST_PASSED", "TC-EV-002 completed successfully")


    def test_filter_by_date_range(self):
        """TC-EV-003: Filter with Date Range"""
        log_step("TEST_START", "TC-EV-003 - Filter by Date Range")

        now = datetime.datetime.now()
        current_day = str(now.day)
        current_year = str(now.year)

        expected_formats = [
            now.strftime("%b %d"),
            now.strftime("%b %d, %Y"),
            now.strftime("%d %b %Y"),
            now.strftime("%B %d, %Y"),
            now.strftime("%d.%m.%Y"),
            f"{current_day} {now.strftime('%b')} {current_year}",
        ]

        log_step("OPEN_DATE_FILTER")
        date_trigger = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//mat-label[contains(., 'Date') or contains(., 'Дата')]")
        ))
        scroll_into_view(self.driver, date_trigger)
        click_with_js(self.driver, date_trigger)

        log_step("SELECT_DATE", f"Selecting day {current_day} (twice for range)")
        day_btn = self.wait.until(EC.element_to_be_clickable(
            (By.XPATH, f"//span[contains(@class, 'cell-content') and normalize-space(text())='{current_day}']")
        ))
        click_with_js(self.driver, day_btn)
        click_with_js(self.driver, day_btn)

        log_step("WAIT_FOR_FILTERED_RESULTS")
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "event-list-item")))

        events = self.driver.find_elements(By.CLASS_NAME, "event-list-item")
        log_step("RESULTS_COUNT", f"Found {len(events)} events after date filter")

        for i, event in enumerate(events):
            actual_date = event.find_element(By.CSS_SELECTOR, "div.date").text.strip()

            is_match = any(expected in actual_date for expected in expected_formats)

            if not is_match:
                log_step("DATE_MISMATCH",
                         f"Card {i+1}: '{actual_date}' (expected one of: {expected_formats})",
                         "WARN")

            self.assertTrue(is_match,
                            f"TC-EV-003: Card {i+1} has wrong date.\n"
                            f"Actual  : {actual_date}\n"
                            f"Expected formats: {expected_formats}")

        log_step("TEST_PASSED", "TC-EV-003 completed successfully")


    def test_unauthorized_event_creation_negative(self):
        """TC-EV-004 [Negative]: Unauthorized Creation Blocked"""
        log_step("TEST_START", "TC-EV-004 - Unauthorized Event Creation (Negative)")

        log_step("CLICK_CREATE_BUTTON")
        create_btn = wait_clickable(self.driver, (By.CSS_SELECTOR, "div.create > button.secondary-global-button"))
        click_with_js(self.driver, create_btn)

        log_step("VERIFY_AUTH_MODAL_APPEARS")
        auth_modal = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, "mat-dialog-container")))
        self.assertTrue(auth_modal.is_displayed(), "TC-EV-004: Auth modal did not appear for guest user")

        log_step("CLOSE_AUTH_MODAL")
        close_btn = wait_clickable(self.driver, (By.CSS_SELECTOR, "app-auth-modal img.cross-btn"))
        click_with_js(self.driver, close_btn)

        self.wait.until(EC.invisibility_of_element_located((By.TAG_NAME, "mat-dialog-container")))
        self.assertIn("/events", self.driver.current_url)

        log_step("TEST_PASSED", "TC-EV-004 (Negative) completed successfully")


    def test_non_existent_search_negative(self):
        """TC-EV-005 [Negative]: Search Non-Existent Event"""
        log_step("TEST_START", "TC-EV-005 - Search Non-Existent Event (Negative)")

        search_query = "xyz123_non_existent_data"

        log_step("OPEN_SEARCH_FIELD")
        search_trigger = wait_clickable(self.driver, (By.CSS_SELECTOR, "div.container-img"))
        click_with_js(self.driver, search_trigger)

        log_step("ENTER_NON_EXISTENT_QUERY", f"Searching for '{search_query}'")
        search_field = wait_element(self.driver, (By.CSS_SELECTOR, "input[placeholder*='Search']"))
        clear_and_type(search_field, search_query + Keys.ENTER)

        log_step("WAIT_FOR_NO_RESULTS_MESSAGE")
        no_results_msg = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(), 'find any results') or contains(text(), 'не знайшли')]")
        ))

        events = self.driver.find_elements(By.CLASS_NAME, "event-list-item")
        self.assertEqual(len(events), 0, "TC-EV-005: Events were found despite non-existent search")

        self.assertTrue(no_results_msg.is_displayed())
        log_step("TEST_PASSED", "TC-EV-005 (Negative) completed successfully")


    def test_search_multiple_terms(self):
        """TC-EV-006: Search with Multiple Terms"""
        log_step("TEST_START", "TC-EV-006 - Parameterized Search with Multiple Terms")

        search_data = ["E", "Eco", "Green", "Event"]

        log_step("OPEN_SEARCH_INTERFACE")
        search_trigger = wait_clickable(self.driver, (By.CSS_SELECTOR, "div.container-img"))
        click_with_js(self.driver, search_trigger)

        search_field = wait_element(self.driver, (By.CSS_SELECTOR, "input[placeholder*='Search']"))

        for term in search_data:
            with self.subTest(search_term=term):
                log_step("CLEAR_AND_TYPE", f"Term: '{term}'")
                clear_and_type(search_field, term + Keys.ENTER)

                log_step("WAIT_FOR_UPDATE", f"Waiting for results of '{term}'")
                self.wait.until(lambda d: d.find_elements(By.CLASS_NAME, "event-list-item") or
                                          d.find_elements(By.XPATH, "//*[contains(text(), 'find any results')]"))

                results = self.driver.find_elements(By.CLASS_NAME, "event-list-item")
                count = len(results)

                if count > 0:
                    try:
                        first_title = self.driver.find_element(By.CLASS_NAME, "event-name").text[:60]
                        log_step("SEARCH_RESULT", f"'{term}' → {count} results (Top: {first_title})")
                    except Exception:
                        log_step("SEARCH_RESULT", f"'{term}' → {count} results")
                else:
                    log_step("SEARCH_RESULT", f"'{term}' → ZERO results", "WARN")

                self.assertGreater(count, 0, f"TC-EV-006: No results for term '{term}'")

        log_step("TEST_PASSED", "TC-EV-006 completed successfully")


if __name__ == "__main__":
    unittest.main(verbosity=2)
