from selenium import webdriver

def create_driver(browser_name):
    if browser_name == "chrome":
        return webdriver.Chrome()

    elif browser_name == "firefox":
        return webdriver.Firefox()

    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

