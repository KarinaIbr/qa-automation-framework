from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.inventory_page import InventoryPage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, '[data-test="error"]')

    # Actions
    def enter_username(self, username):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return InventoryPage(self.driver)

    def is_error_message_visible(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).is_displayed()

    def get_error_message_text(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text


