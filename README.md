# GreenCity — Events Page Testing
> **SoftServe Academy · QA Homework**

---

# Project Description / Опис проєкту

**EN:** This repository contains a structured set of manual test cases and automated Selenium tests for the **Events** page of the GreenCity web application. The project demonstrates skills in test documentation, requirements analysis, Page Object Model design, and test automation using Python + Selenium + Allure.

**UA:** Репозиторій містить структурований набір ручних тест-кейсів та автоматизованих Selenium-тестів для сторінки **Events** вебзастосунку GreenCity. Проєкт демонструє навички написання тестової документації, аналізу вимог, побудови Page Object Model та автоматизації тестування за допомогою Python + Selenium + Allure.

---

# Repository Structure / Структура репозиторію

```bash
greencity-tests/
├── src/
│   ├── components/
│   │   ├── __init__.py
│   │   ├── base_component.py
│   │   ├── event_card.py
│   │   ├── filter_panel.py
│   │   └── header.py
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── base_page.py
│   │   └── events_page.py          # Main Page Object used by the test suite
│   └── __init__.py
├── pages/                          # Legacy page helpers
│   ├── components/
│   │   └── event_card_components.py
│   ├── base_page.py
│   └── events_page.py
├── test-cases/
│   └── events-page-tests.md        # Manual test cases (TC-EV-001 – TC-EV-006)
├── tests/
│   ├── conftest.py                 # Fixtures (driver setup/teardown)
│   ├── test_events_page_lesson6.py # Production-ready tests (pytest + Allure + POM)
│   ├── test_events_page_lesson5.py # Intermediate implementation (unittest + POM)
│   ├── test_events_page.py         # Initial raw Selenium implementation
│   └── utils.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

# Test Cases / Тест-кейси

📄 `events-page-tests.md`

| ID         | Title                                 | Priority | Type     |
|------------|---------------------------------------|----------|----------|
| TC-EV-001  | Filter by Type (Social)               | Medium   | Positive |
| TC-EV-002  | Search by Name                        | High     | Positive |
| TC-EV-003  | Filter by Date Range                  | Medium   | Positive |
| TC-EV-004  | Unauthorized Event Creation           | Medium   | Negative |
| TC-EV-005  | Search for a Non-existent Event       | Low      | Negative |
| TC-EV-006  | Parameterized Search (Multiple Terms) | Medium   | Positive |

---

# Automated Tests / Автоматизовані тести

The repository contains three iterations of automated tests that demonstrate the progression of automation skills — from basic Selenium scripts to a production-ready test framework.

## ✅ `test_events_page_lesson6.py` — Production Ready (pytest + Allure + POM)

Main test suite built using modern automation practices.

- **Framework:** pytest + Allure for detailed reporting.
- **Design Pattern:** Page Object Model (POM). Page interaction logic is separated into `src/pages/events_page.py`.
- **Code Quality:** Uses fixtures (`conftest.py`) and parameterization for cleaner and reusable tests.

| Test Method                  | Covers    | Allure Story |
| ---------------------------- | --------- | ------------- |
| `test_filter_by_type`        | TC-EV-001 | Filters       |
| `test_search_by_name`        | TC-EV-002 | Search        |
| `test_parameterized_search`  | TC-EV-006 | Search        |

```bash
pytest tests/test_events_page_lesson6.py --alluredir=allure-results
allure serve allure-results
```

## 📘 `test_events_page_lesson5.py` — Intermediate (unittest + POM)

Second iteration of the framework. Introduces the Page Object Model while still using Python’s built-in `unittest` framework.

- Uses page classes for locating and interacting with elements.
- Step logging implemented through a custom `log_step` utility.
- Reporting is console-based without Allure integration.

```bash
python -m unittest tests/test_events_page_lesson5.py -v
```

## 📗 `test_events_page.py` — Legacy / Initial (unittest)

First iteration based on raw Selenium.

- No Page Object Model: locators and test logic are placed directly inside test methods.
- Direct WebDriver management in `setUp` and `tearDown`.

```bash
python -m unittest tests/test_events_page.py -v
```

---

# How to Run Tests / Як запустити тести

**Prerequisites:** Python 3.8+ and Google Chrome installed.

```bash
# 1. Clone the repository
git clone https://github.com/IOANN-K/greencity-tests.git
cd greencity-tests

# 2. Install dependencies
pip install -r requirements.txt
```

## Run all tests

```bash
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

## Run a specific test suite

```bash
# Main production-ready suite
pytest tests/test_events_page_lesson6.py -v

# Intermediate suite
python -m unittest tests/test_events_page_lesson5.py -v

# Legacy suite
python -m unittest tests/test_events_page.py -v
```

## Dependencies (`requirements.txt`)

```txt
selenium==4.41.0
webdriver-manager==4.0.2
pytest==9.0.3
allure-pytest==2.16.0
```

---

# Tested Page / Тестована сторінка

🌐 https://www.greencity.cx.ua/#/greenCity/events

## Environment

- OS: Windows 11
- Browser: Chrome / Brave (latest versions)
- Resolution: 1920×1080

---

# Author / Автор

**Kozii Ivan / Козій Іван**  
SoftServe IT Academy · QA Course
