from selenium.webdriver.common.by import By

class EventCardComponent:
    def __init__(self, container):
        self.container = container

    def get_name(self):
        # Шукаємо заголовок всередині конкретної картки
        return self.container.find_element(By.CSS_SELECTOR, ".title").text.strip()

    def click_more(self):
        self.container.find_element(By.CSS_SELECTOR, ".more-details-link").click()