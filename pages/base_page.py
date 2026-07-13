from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import TIMEOUT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, TIMEOUT)

    def open(self, url):
        self.driver.get(url)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def wait_for_visible_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_url_contains(self, text):
        return self.wait.until(EC.url_contains(text))

    def wait_for_clickable_element(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click_element(self, locator):
        element = self.wait_for_clickable_element(locator)
        self.scroll_to_element(element)
        element.click()

    def js_click(self, locator):
        element = self.wait_for_clickable_element(locator)
        self.scroll_to_element(element)
        self.driver.execute_script("arguments[0].click();", element)
