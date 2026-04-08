import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
 
 
def log_step(step: str, message: str = "DONE", status: str = "INFO"):
    """Уніфікований логгер"""
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] [{status}] {step:35} → {message}")
 
 
def wait_element(driver, locator, timeout=15):
    """Чекає та повертає видимий елемент"""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )
 
 
def wait_clickable(driver, locator, timeout=15):
    """Чекає, поки елемент стане клікабельним"""
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
 
 
def click_with_js(driver, element):
    """Клік через JS (для Angular/Material елементів)"""
    driver.execute_script("arguments[0].click();", element)
 
 
def scroll_into_view(driver, element):
    """Скролить до елемента перед кліком (потрібно для Angular Material dropdown)"""
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
 
 
def clear_and_type(field, text):
    """Очищає поле та вводить текст"""
    field.click()
    field.send_keys(Keys.CONTROL + "a")
    field.send_keys(Keys.BACKSPACE)
    field.send_keys(text)
 
 
def wait_text_in_element(driver, locator, text, timeout=15):
    """Чекає, поки в елементі з'явиться потрібний текст"""
    return WebDriverWait(driver, timeout).until(
        EC.text_to_be_present_in_element(locator, text)
    )