import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
 
 
def log_step(step: str, message: str = "DONE", status: str = "INFO"):
    """Unified logger"""
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"[{timestamp}] [{status}] {step:35} → {message}")
 
 
def wait_element(driver, locator, timeout=15):
    """Wait till element is visible and return it"""
    return WebDriverWait(driver, timeout).until(
        EC.visibility_of_element_located(locator)
    )
 
 
def wait_clickable(driver, locator, timeout=15):
    """Wait till element is clickable and return it"""
    return WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable(locator)
    )
 
 
def click_with_js(driver, element):
    """Click through JS (for Angular/Material elements)"""
    driver.execute_script("arguments[0].click();", element)
 
 
 
 
def clear_and_type(field, text):
    """Clears the field and types the text"""
    field.click()
    field.send_keys(Keys.CONTROL + "a")
    field.send_keys(Keys.BACKSPACE)
    field.send_keys(text)
 
 
def wait_text_in_element(driver, locator, text, timeout=15):
    """Wait till the specified text is present in the element"""
    return WebDriverWait(driver, timeout).until(
        EC.text_to_be_present_in_element(locator, text)
    )