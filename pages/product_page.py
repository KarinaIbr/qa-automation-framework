from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    # Locators
    BACK_TO_PRODUCTS = (By.CSS_SELECTOR, '[data-test="back-to-products"]')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')

    def __init__(self, driver):
        super().__init__(driver)

    # Methods
    def is_back_to_products_visible(self):
        return self.driver.find_element(*self.BACK_TO_PRODUCTS).is_displayed()

    def get_product_title(self):
        return self.wait_for_visible_element(self.PRODUCT_TITLE).text

    def click_back_to_products(self):
        self.wait_for_clickable_element(self.BACK_TO_PRODUCTS).click()
        self.wait_for_url_contains("inventory.html")


