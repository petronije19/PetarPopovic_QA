from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_and_click(self, locator):
        element = self.wait_for_element_clickable(locator)
        element.click()

    def get_element_text(self, locator):
        element = self.wait_for_element_visible(locator)
        return element.text
    
    def get_current_url_path(self):
        from urllib.parse import urlparse
        parsed_url = urlparse(self.driver.current_url)
        return parsed_url
    
    def scroll_to_element(self, locator):
        element = self.wait_for_element_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.wait.until(EC.visibility_of(element)) 