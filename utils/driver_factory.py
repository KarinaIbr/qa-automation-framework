from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def create_driver(browser_name, headless=False):

    if browser_name == "chrome":
        options = ChromeOptions()

        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")

        return webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()

        if headless:
            options.add_argument("-headless")
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")

        return webdriver.Firefox(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

