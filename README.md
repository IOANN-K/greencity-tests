# GreenCity Events Page Testing

### Project description / Опис проєкту 
EN: This repository contains a basic set of test cases to test the functionality of the Events page of the GreenCity web application. The purpose of the work is to demonstrate skills in structuring documentation and analyzing requirements.

UA: Цей репозиторій містить базовий набір тест-кейсів для перевірки функціональності сторінки подій (Events) веб-застосунку GreenCity. Мета роботи - продемонструвати навички структурування документації та аналізу вимог.

Test Cases:  
https://github.com/IOANN-K/greencity-tests/blob/main/test-cases/events-page-tests.md

### Tested page / Тестована сторінка
https://www.greencity.cx.ua/#/greenCity/events

### Author / Автор
Kozii Ivan / Козій Іван

## Discovered Issues / Виявлені дефекти
During test case creation, the following issues were identified:

1. **Event Search Issue (TC-EV-002 Fail) (High):**  
Searching for a specific event by its full name often returns "We didn't find any results matching to this search", while one-letter search works. 
2. **Broken Date Range Logic (TC-EV-003) (High):**
   - **Issue:** The date filter exhibits undefined behavior. Selecting a range (e.g., Feb 20 – Feb 22) fails to show relevant events for those dates, but unexpectedly displays events from the past (e.g., Feb 19).
   - **Technical Observation:** This indicates a logic error in date parsing or a Timezone Offset issue (UTC vs Local Time).
   - **Impact:** TC-EV-003 cannot be verified successfully as the system returns incorrect and unrelated data.
