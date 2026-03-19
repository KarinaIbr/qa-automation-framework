from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    PRODUCTS_TITLE = (By.CSS_SELECTOR, '[data-test="title"]')
    INVENTORY_ITEMS = (By.CSS_SELECTOR, '[data-test="inventory-item"]')
    FIRST_PRODUCT_TITLE = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')

    # Action
    def is_products_title_visible(self):
        return self.driver.find_element(*self.PRODUCTS_TITLE).is_displayed()

    def get_inventory_items_count(self):
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))

    def open_first_product(self):
        self.driver.find_element(*self.FIRST_PRODUCT_TITLE).click()

    def get_first_product_title(self):
        return self.driver.find_element(*self.FIRST_PRODUCT_TITLE).text
