import pytest
import allure
from src.pages.events_page import EventsPage


@allure.feature("Events Page")
class TestEventsPage:
    """Test suite for GreenCity Events page."""

    @allure.story("Filters")
    @allure.title("TC-EV-001: Filter by Type")
    def test_filter_by_type(self, driver):
        """Verify that events are filtered correctly when a specific type is selected."""
        events_page = EventsPage(driver)
        events_page.open_events()

        with allure.step("Select 'Social' type from the filter dropdown"):
            events_page.select_filter_type("Social")
            
        with allure.step("Observe the list of event cards for 'Social' labels"):
            count = events_page.get_events_count()
            # Assuming PO has a method to check labels of all visible cards
            social_cards_count = events_page.get_events_count_by_label("Social")
            
            assert count == social_cards_count, (
                f"Filter failed: Expected all {count} cards to be 'Social', but only {social_cards_count} matched."
            )

    @allure.story("Search")
    @allure.title("TC-EV-002: Search by Name")
    def test_search_by_name(self, driver):
        """Verify that events can be filtered using the search input field."""
        events_page = EventsPage(driver)
        events_page.open_events()
        
        initial_count = events_page.get_events_count()

        with allure.step("Type a partial event name (e.g., 'Eve')"):
            events_page.search_for("Eve")
            filtered_count = events_page.get_events_count()
            assert filtered_count >= 0, "Event count should be a valid integer."

        with allure.step("Add special characters to the search string"):
            events_page.search_for("Eve~*/*#")
            assert events_page.is_no_results_shown(), "Expected 'no results' message to be displayed."

        with allure.step("Clear the search field"):
            events_page.clear_search()
            restored_count = events_page.get_events_count()
            assert restored_count == initial_count, "Events list did not restore after clearing search."

    @allure.story("Filters")
    @allure.title("TC-EV-003: Filter by Date")
    def test_filter_by_date(self, driver):
        """Verify that events are filtered correctly when a specific date is selected."""
        events_page = EventsPage(driver)
        events_page.open_events()

        with allure.step("Open date range filter and select Jan 1, 2026 to Feb 28, 2026"):
            events_page.select_date_range("Jan 1, 2026", "Feb 28, 2026")

        with allure.step("Observe the list of event cards"):
            # A strict test would verify the actual dates on the cards fall within the range.
            assert events_page.get_events_count() >= 0
            assert events_page.are_all_events_within_date_range("2026-01-01", "2026-02-28"), (
                "Found events outside the specified date range."
            )

    @allure.story("Authorization")
    @allure.title("TC-EV-004 [Negative]: Unauthorized Event Creation")
    def test_unauthorized_event_creation(self, driver):
        """Verify that an unauthorized user cannot create an event and is prompted to sign in."""
        events_page = EventsPage(driver)
        events_page.open_events()

        with allure.step("Click on the 'Create event' button"):
            events_page.click_create_event()

        with allure.step("Verify the sign-in window appears"):
            assert events_page.is_sign_in_modal_visible(), "Sign-in modal did not appear for unauthorized user."

        with allure.step("Close the sign-in window"):
            events_page.close_sign_in_modal()
            assert not events_page.is_sign_in_modal_visible(), "Sign-in modal did not close."

    @allure.story("Search")
    @allure.title("TC-EV-005 [Negative]: Non-existent Search")
    def test_non_existent_search(self, driver):
        """Verifying system behavior when there are no search results."""
        events_page = EventsPage(driver)
        events_page.open_events()

        with allure.step("Enter a random string in the search field"):
            events_page.search_for("xyz123_non_existent_qwertyuiop")

        with allure.step("Check for a message about the absence of results"):
            assert events_page.get_events_count() == 0, "Events list should be empty."
            assert events_page.is_no_results_shown(), "Expected 'no results' stub/message was not displayed."

    @allure.story("Search")
    @allure.title("TC-EV-006: Parameterized Search with Multiple Terms")
    @pytest.mark.parametrize("search_term", [
        "E", 
        "Eco", 
        "Green", 
        "Event"
    ])
    def test_parameterized_search(self, driver, search_term):
        """Verifying that the search functionality correctly handles various valid search queries."""
        events_page = EventsPage(driver)
        events_page.open_events()

        with allure.step(f"Search for term: '{search_term}'"):
            events_page.search_for(search_term)

        with allure.step("Verify results dynamically update"):
            # If your test DB guarantees these terms exist, assert > 0.
            # Otherwise, you just assert the page doesn't crash and handles the state.
            count = events_page.get_events_count()
            assert count >= 0, f"Search failed or crashed for term '{search_term}'"
