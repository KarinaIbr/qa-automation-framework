from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):

    # Locators
    CHECKOUT_PAGE_TITLE = (By.CSS_SELECTOR, '[data-test="title"]')
    FIRST_NAME_FIELD = (By.CSS_SELECTOR,'[data-test="firstName"]')

    def __init__(self, driver):
        super().__init__(driver)

    def is_loaded(self):
        return (
                self.is_element_visible(self.FIRST_NAME_FIELD)
                and "checkout-step-one" in self.get_current_url()
                and self.get_checkout_page_title() == "Checkout: Your Information"
        )

    def get_checkout_page_title(self):
        return self.wait_for_visible_element(self.CHECKOUT_PAGE_TITLE).text

    def get_current_url(self):
        return self.driver.current_url

