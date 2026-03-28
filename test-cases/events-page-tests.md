# Test-cases for GreenCity Events Page

## TC-EV-001: Filter by Type
**Title:**  
Verify that events are filtered correctly when a specific type is selected from the dropdown.

**Related Requirement:**  
As a user, I want to filter events by type so that I can find relevant activities quickly.

**Date Created**  
2026-03-28

**Author**  
Kozii Ivan

**Priority**  
Medium

**Preconditions:**
- URL: https://www.greencity.cx.ua/#/greenCity/events
- Multiple events with different types (e.g., "Economic", "Social") exist in the system.

| Step | Action | Data | Expected Result |
| :--- | :--- | :--- | :--- |
| 1 | Click on the "Type" filter dropdown | - | The dropdown list expands, showing available types. |
| 2 | Select a specific type from the list | Select: "Social" | The selected type is displayed in the filter field; the list collapses. |
| 3 | Observe the list of event cards | - | The event counter updates correctly, and only events with the "Social" label are displayed. |

**Postconditions**  
No data changes

**Environment**  
**OS:** Windows 11  
**Browser:** Brave (Latest version)  
**Resolution:** 1920x1080


**Screenshots**  
N/A

**Additional Context**  
N/A

---

## TC-EV-002: Search by Name
**Title:**  
Verify that events can be filtered using the search input field.

**Related Requirement:**  
As a user, I want to filter events by search input so that I can find relevant activities quickly.

**Date Created**  
2026-03-28

**Author**  
Kozii Ivan

**Priority**  
High

**Preconditions:**
- URL: https://www.greencity.cx.ua/#/greenCity/events
- At least one event with a known title exists (e.g., "Event").

| Step | Action | Data | Expected Result |
| :--- | :--- | :--- | :--- |
| 1 | Type a partial event name (3+ characters) | "Eve" | Results update dynamically without reloading the page; only events containing "Eve" are shown. |
| 2 | Add special characters to the search string | "~*/*#" | The list displays a message: "We didn't find any results matching to this search"; UI does not break/crash. |
| 3 | Clear the search field | - | The filter is reset; the full list of events is restored to the initial state. |

**Postconditions**  
No data changes

**Environment**  
**OS:** Windows 11  
**Browser:** Brave (Latest version)  
**Resolution:** 1920x1080


**Screenshots**  
N/A

**Additional Context**  
N/A

---

## TC-EV-003: Filter by Date
**Title:**  
Verify that events are filtered correctly when a specific date is selected.

**Related Requirement:**  
As a user, I want to filter events by date so that I can find relevant activities quickly.

**Date Created**  
2026-03-28

**Author**  
Kozii Ivan

**Priority**  
Medium

**Preconditions:**
- URL: https://www.greencity.cx.ua/#/greenCity/events
- At least one event with a known date exists (e.g., "Feb 20, 2026").

| Step | Action | Data | Expected Result |
| :--- | :--- | :--- | :--- |
| 1 | Click on the "Date range" filter dropdown | - | The calendar picker expands. |
| 2 | Select a start date from the calendar | Date: "Jan 1, 2026" | The start date in calendar is selected. |
| 3 | Select a end date from the calendar | Date: "Feb 28, 2026" | The end date in calendar is selected. Selected range date event is displayed in the filter field; the calendar collapses. |
| 4 | Observe the list of event cards | - | Only events scheduled between January 1, 2026, and February 28, 2026, are displayed. |

**Postconditions**  
No data changes

**Environment**  
**OS:** Windows 11  
**Browser:** Brave (Latest version)  
**Resolution:** 1920x1080


**Screenshots**  
N/A

**Additional Context**  
N/A

---

## TC-EV-004 [Negative]: Unauthorized Event Creation
**Title:**  
Verify that unauthorized user cannot create event and is prompted to sign in

**Related Requirement:**  
As a system, I want to restrict event creation to registered users only to ensure data quality.

**Date Created**  
2026-03-28

**Author**  
Kozii Ivan

**Priority**  
Medium

**Preconditions:**
- URL: https://www.greencity.cx.ua/#/greenCity/events
- User is non-registered

| Step | Action | Data | Expected Result |
| :--- | :--- | :--- | :--- |
| 1 | Click on the "Create event" button | - | The sign in window appears |
| 2 | Close sign in window | - | The login modal closes, and the user remains on the Events page |

**Postconditions**  
No data changes

**Environment**  
**OS:** Windows 11  
**Browser:** Brave (Latest version)  
**Resolution:** 1920x1080


**Screenshots**  
N/A

**Additional Context**  
N/A

---

## TC-EV-005 [Negative]: Non-existent Search
**Title:**  
Verifying system behavior when there are no search results

**Related Requirement:**  
As a user, I want to filter events by search input so that I can find relevant activities quickly.

**Date Created**  
2026-03-28

**Author**  
Kozii Ivan

**Priority**  
Low

**Preconditions:**
- URL: https://www.greencity.cx.ua/#/greenCity/events

| Step | Action | Data | Expected Result |
| :--- | :--- | :--- | :--- |
| 1 | Enter a random string in the search field | "xyz123_non_existent_qwertyuiop" | The list of events is empty |
| 2 | Check for a message about the absence of results | - | A text message (for example, "We didn't find any results matching to this search") or a corresponding stub is displayed |

**Postconditions**  
No data changes

**Environment**  
**OS:** Windows 11  
**Browser:** Brave (Latest version)  
**Resolution:** 1920x1080


**Screenshots**  
N/A

**Additional Context**  
N/A
