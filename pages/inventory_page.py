from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.cart_page import CartPage
from selenium.webdriver.support.select import Select


class InventoryPage(BasePage):

    # Locators
    PRODUCTS_TITLE = (By.CSS_SELECTOR, '[data-test="title"]')
    INVENTORY_ITEMS = (By.CSS_SELECTOR, '[data-test="inventory-item"]')
    INVENTORY_ITEM_NAME = (By.CSS_SELECTOR, '[data-test="inventory-item-name"]')
    INVENTORY_ITEM_PRICE = (By.CSS_SELECTOR, '[data-test="inventory-item-price"]')
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ITEM_CONTAINER_FROM_ANCHOR = (By.XPATH, './ancestor::div[@data-test="inventory-item"][1]')
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")
    SHOPPING_CART_BADGE = (By.CSS_SELECTOR, '[data-test="shopping-cart-badge"]')
    SHOPPING_CART_LINK = (By.CSS_SELECTOR, '[data-test="shopping-cart-link"]')
    INVENTORY_SORT_CONTAINER = (By.CSS_SELECTOR, '[data-test="product-sort-container"]')

    def __init__(self, driver):
        super().__init__(driver)

    # Methods
    def is_products_title_visible(self):
        return self.driver.find_element(*self.PRODUCTS_TITLE).is_displayed()

    def get_inventory_items_count(self):
        return len(self.driver.find_elements(*self.INVENTORY_ITEMS))

    def open_first_product(self):
        self.driver.find_element(*self.INVENTORY_ITEM_NAME).click()

    def get_first_product_title(self):
        return self.driver.find_element(*self.INVENTORY_ITEM_NAME).text

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

    def open_cart(self):
        self.driver.find_element(*self.SHOPPING_CART_LINK).click()
        cart_page = CartPage(self.driver)
        return cart_page

    def _get_backpack_container(self):
        backpack_button = self.driver.find_element(*self.ADD_TO_CART_BACKPACK)
        item_container = backpack_button.find_element(*self.ITEM_CONTAINER_FROM_ANCHOR)
        return item_container

    def get_backpack_name(self):
        item_container = self._get_backpack_container()
        return item_container.find_element(*self.INVENTORY_ITEM_NAME).text

    def get_backpack_price(self):
        item_container = self._get_backpack_container()
        return item_container.find_element(*self.INVENTORY_ITEM_PRICE).text

    def sort_products_by_price_low_to_high(self):
        sort_low_to_high = Select(self.driver.find_element(*self.INVENTORY_SORT_CONTAINER))
        sort_low_to_high.select_by_visible_text("Price (low to high)")

    def get_all_product_prices(self):
        all_prices = self.driver.find_elements(*self.INVENTORY_ITEM_PRICE)
        price_values = [float(price.text.replace("$", "")) for price in all_prices]
        return price_values











