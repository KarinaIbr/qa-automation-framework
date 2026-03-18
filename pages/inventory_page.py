from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    PRODUCTS_TITLE = (By.CSS_SELECTOR, '[data-test="title"]')

    # Action
    def is_products_title_visible(self):
        return self.driver.find_element(*self.PRODUCTS_TITLE).is_displayed()
