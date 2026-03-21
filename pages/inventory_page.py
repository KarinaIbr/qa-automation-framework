from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    PRODUCTS_TITLE = (By.CSS_SELECTOR, '[data-test="title"]')
    INVENTORY_ITEMS = (By.CSS_SELECTOR, '[data-test="inventory-item"]')
    FIRST_PRODUCT_TITLE = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    SHOPPING_CART_BADGE = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')

    # Action
    def is_products_title_visible(self):
        return self.driver.find_element(*self.PRODUCTS_TITLE).is_displayed()

    def get_inventory_items_count(self):
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))

    def open_first_product(self):
        self.driver.find_element(*self.FIRST_PRODUCT_TITLE).click()

    def get_first_product_title(self):
        return self.driver.find_element(*self.FIRST_PRODUCT_TITLE).text

    def get_backpack_button_text(self):
        return self.driver.find_element(*self.ADD_TO_CART_BACKPACK).text

    def click_add_to_cart_backpack_button(self):
        self.driver.find_element(*self.ADD_TO_CART_BACKPACK).click()

    def get_remove_backpack_text(self):
        return self.driver.find_element(*self.REMOVE_BACKPACK).text

    def is_shopping_cart_badge_visible(self):
        return len(self.driver.find_elements(*self.SHOPPING_CART_BADGE)) > 0

    def get_shopping_cart_badge_text(self):
        return self.driver.find_element(*self.SHOPPING_CART_BADGE).text

    def click_remove_backpack_button(self):
        self.driver.find_element(*self.REMOVE_BACKPACK).click()




