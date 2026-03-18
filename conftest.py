import datetime
import pytest
from config.settings import BASE_URL
from utils.driver_factory import create_driver

BROWSERS =["chrome", "firefox"]

@pytest.fixture(params = BROWSERS, scope = "function")
def driver(request):
    browser_name = request.param
    driver = create_driver(browser_name)

    driver.get(BASE_URL)

    yield driver

    driver.quit()


def pytest_configure(config):
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%m-%S")
    report_path = f"reports/report_{now}.html"
    config.option.htmlpath = report_path

