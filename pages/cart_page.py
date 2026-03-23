from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):

    # Locators
    CART_PAGE_TITLE = (By.CSS_SELECTOR, '[data-test="title"]')
    CART_ITEM_NAME = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    CART_ITEM_PRICE = (By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
    CART_ITEM_QUANTITIES = (By.CSS_SELECTOR, '[data-test="item-quantity"]')

    def __init__(self, driver):
        super().__init__(driver)

    # Methods
    def get_cart_page_title(self):
        return self.wait_for_visible_element(self.CART_PAGE_TITLE).text

    def get_cart_item_name(self):
        return self.driver.find_element(*self.CART_ITEM_NAME).text

    def get_cart_item_price(self):
        return self.driver.find_element(*self.CART_ITEM_PRICE).text

    def get_cart_item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEM_QUANTITIES))

