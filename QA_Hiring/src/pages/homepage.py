from selenium.webdriver.common.by import By
from src.pages.basepage import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from urllib.parse import urlparse


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
   
    HOME_PAGE_IDENTIFIERS = [
        (By.XPATH, "//span[contains(., 'Book your next fishing trip')]"),
        (By.CSS_SELECTOR, "[data-testid='search-form-check-availability-button']"),
        (By.XPATH, "//p[contains(., 'Discover top-rated fishing charters')]"),
        (By.XPATH, "//div[contains(., \"FishingBooker – the world's largest online travel fishing company\")]")
    ]

    AMAZING_DESTINATIONS_SECTION = (By.ID, "popular-destinations")

    SECOND_DESTINATION_CARD = (By.CSS_SELECTOR, "[data-testid='popular-destination-card-1']")

    FISHING_SEASON_HEADING = (By.ID, "destination-fishing-seasons")

    RIGHT_ARROW_BUTTON = (By.CSS_SELECTOR, "#destination-fishing-seasons [data-testid='carousel-button-next']")

    MONTH_ELEMENT = (By.XPATH, "//span[normalize-space()='October']")

    
    def is_homepage_loaded(self):
        for locator in self.HOME_PAGE_IDENTIFIERS:
            try:
                temp_wait = WebDriverWait(self.driver, 5) # Kratak timeout za svaki identifikator
                temp_wait.until(EC.visibility_of_element_located(locator))
                return True 
            
            except TimeoutException:
                continue

            except Exception as e:
                continue

        return False
    
    def click_second_destination_card(self):
        self.scroll_to_element(self.AMAZING_DESTINATIONS_SECTION)
        self.wait_and_click(self.SECOND_DESTINATION_CARD)

    
    def validate_url_contains_text(self, expected_text):
        current_url = self.driver.current_url
        return expected_text in current_url

    def is_right_arrow_visible_in_fishing_season(self):
        self.scroll_to_element(self.FISHING_SEASON_HEADING)

        try:
            element = self.wait_for_element_visible(self.RIGHT_ARROW_BUTTON)
            return element is not None
        except TimeoutException:
            return False
    
    def click_right_arrow(self):
        element = self.wait_for_element_visible(self.RIGHT_ARROW_BUTTON)
        self.driver.execute_script("arguments[0].click();", element)
    
    def is_new_month_loaded(self):
        return self.wait_for_element_visible(self.MONTH_ELEMENT) is not None
    
    def get_current_url_path(self):
        parsed_url=urlparse(self.driver.current_url)
        return parsed_url.path