from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    BACK_TO_PRODUCTS = (By.CSS_SELECTOR, '[data-test="back-to-products"]')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')

    # Action
    def is_back_to_products_visible(self):
        return self.driver.find_element(*self.BACK_TO_PRODUCTS).is_displayed()

    def get_product_title(self):
        return self.driver.find_element(*self.PRODUCT_TITLE).text

    def click_back_to_products(self):
        self.driver.find_element(*self.BACK_TO_PRODUCTS).click()


