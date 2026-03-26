import datetime
import pytest
import allure
from config.settings import BASE_URL
from utils.driver_factory import create_driver


BROWSERS = ["chrome", "firefox"]

# Register custom pytest command-line options
def pytest_addoption(parser):
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run tests in headless mode"
    )

# Create browser driver for each test and clean it up after execution
@pytest.fixture(params=BROWSERS, scope="function")
def driver(request):
    browser_name = request.param
    headless = request.config.getoption("--headless")

    driver = create_driver(browser_name, headless=headless)
    driver.get(BASE_URL)

    yield driver

    # Attach screenshot to Allure report if test fails
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        screenshot = driver.get_screenshot_as_png()
        allure.attach(screenshot, name="failure_screenshot", attachment_type=allure.attachment_type.PNG)

    driver.quit()

def pytest_configure(config):
    now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.htmlpath = f"reports/report_{now}.html"

# Save pytest test result on the current test item
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

def pytest_sessionfinish(session, exitstatus):
    with open("allure-results/environment.properties", "w") as env_file:
        env_file.write("project_name=QA Automation Framework\n"
                       "app_under_test=Swag Labs\n"
                       "language=Python\n"
                       "test_framework=pytest\n"
                       "ui_tool=Selenium\n")
