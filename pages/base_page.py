from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def wait_for_visible_element(self, locator):
        wait = WebDriverWait(self.driver, TIMEOUT)
        return wait.until(EC.visibility_of_element_located(locator))

    def wait_for_url_contains(self, text):
        wait = WebDriverWait(self.driver, TIMEOUT)
        return wait.until(EC.url_contains(text))

    def wait_for_clickable_element(self, locator):
        wait = WebDriverWait(self.driver, TIMEOUT)
        return wait.until(EC.element_to_be_clickable(locator))

    def click_element(self, locator):
        element = self.wait_for_clickable_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)
