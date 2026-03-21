import datetime
import pytest
from config.settings import BASE_URL
from utils.driver_factory import create_driver

BROWSERS = ["chrome", "firefox"]

def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode"
    )

@pytest.fixture(params=BROWSERS, scope="function")
def driver(request):
    browser_name = request.param
    headless = request.config.getoption("--headless")

    driver = create_driver(browser_name, headless=headless)
    driver.get(BASE_URL)

    yield driver

    driver.quit()

def pytest_configure(config):
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"reports/report_{now}.html"
