# UI Automation Framework

[**View Live Allure Report**](https://karinaibr.github.io/qa-automation-framework/)

UI test automation framework for Swag Labs using Python, Selenium WebDriver, and pytest.

The project covers login, inventory, product sorting, cart behavior, and checkout navigation. Tests are organized using Page Object Model, with browser interactions separated from test assertions.

## Test Coverage

**Login & Access Control**
- Successful login
- Invalid and empty credentials
- Locked-out user
- Unauthorized access to the inventory page

**Inventory**
- Page loading and product visibility
- Product count verification
- Opening product details and returning to inventory
- Price sorting from low to high

**Cart & Checkout**
- Empty cart after login
- Adding and removing products
- Cart badge and button state changes
- Product name and price verification
- Cart state after page refresh
- Checkout navigation

## Framework Structure

- `pages/` contains Page Objects and shared `BasePage` methods for element interactions and waits.
- `tests/` contains tests grouped by login, inventory, and cart.
- `utils/driver_factory.py` handles Chrome, Firefox, and headless browser setup.
- `config/settings.py` stores the application URL and timeout configuration.
- `conftest.py` manages browser fixtures, test lifecycle, failure screenshots, and reporting hooks.
- `.github/workflows/ci.yml` runs the test suite through GitHub Actions.

## Tech Stack

Python, Selenium WebDriver, pytest, pytest-html, Allure Report, GitHub Actions, GitHub Pages.

## Running Tests Locally

Clone the repository and install dependencies:

```bash
git clone https://github.com/KarinaIbr/qa-automation-framework.git
cd qa-automation-framework
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Chrome and Firefox should be installed locally.

Run the tests:

```bash
pytest --headless --alluredir=allure-results
```

The browser fixture runs tests against both Chrome and Firefox. Remove `--headless` to watch the tests execute in the browser.

Run a specific test area:

```bash
pytest tests/login -v --alluredir=allure-results
pytest tests/inventory -v --alluredir=allure-results
pytest tests/cart -v --alluredir=allure-results
```

To generate and open an Allure report (requires Allure CLI):

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## CI & Reporting

GitHub Actions runs the test suite on pushes and pull requests.

The workflow runs headless browser tests, collects Allure results, and generates an HTML report. Failed tests include screenshots, the current URL, and page source to help investigate failures.

Reports are saved as GitHub Actions artifacts. The Allure report is also published to GitHub Pages after successful runs on `main`.

[**Open Published Allure Report**](https://karinaibr.github.io/qa-automation-framework/)

## Click Handling

Native Selenium clicks were causing repeated failures in Chrome CI. I tried a few approaches, including native clicks with a JavaScript fallback, but eventually switched back to JS clicks after scrolling elements into view.

The current implementation is in `BasePage`. I may revisit this if I find a more reliable solution.
