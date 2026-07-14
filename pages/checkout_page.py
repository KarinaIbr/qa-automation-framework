from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):

    # Locators
    CHECKOUT_PAGE_TITLE = (By.CSS_SELECTOR, '[data-test="title"]')

    def __init__(self, driver):
        super().__init__(driver)

    def get_checkout_page_title(self):
        return self.wait_for_visible_element(self.CHECKOUT_PAGE_TITLE).text
