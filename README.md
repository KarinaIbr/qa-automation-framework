# QA Automation Framework

## Live Allure Report

[Open UI Allure Report](https://karinaibr.github.io/qa-automation-framework/)

A UI test automation framework for Swag Labs built with Python, Selenium, and pytest.

It focuses on core user flows, maintainable Page Objects, stable browser execution, and clear test reporting.

## Key Features

- Page Object Model with clear separation between page logic and test logic
- Reusable `BasePage` methods for waits, clicks, and common browser actions
- Browser setup managed through a centralized driver factory
- Cross-browser execution with Chrome and Firefox
- Headless execution for local and CI runs
- Automatic screenshots on test failure
- Allure reporting with readable test results
- GitHub Actions CI for push and pull request validation
- Published GitHub Pages report for quick review

## Tech Stack

- Python
- Selenium
- pytest
- pytest-html
- Allure Report
- GitHub Actions
- GitHub Pages

## Project Structure

```text
qa-automation-framework/
├── .github/
│   └── workflows/
│       └── ci.yml
├── config/
│   └── settings.py
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── product_page.py
│   └── cart_page.py
├── tests/
│   ├── login/
│   ├── inventory/
│   └── cart/
├── utils/
│   └── driver_factory.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Current Coverage

### Login

The test suite currently covers:

- Successful login
- Invalid credentials validation
- Empty username validation
- Empty password validation
- Empty username and password validation

### Inventory

The test suite currently covers:

- Inventory page loading
- Product list visibility
- Opening the first product from the inventory page
- Back to products navigation
- Sorting products by price from low to high

### Cart

The test suite currently covers:

- Adding a product to the cart
- Verifying button state after adding a product
- Verifying cart badge after adding a product
- Removing a product from the cart
- Verifying button state after removing a product
- Verifying cart badge after removing a product
- Verifying product name and price in the cart

## How to Run Locally

```bash
git clone https://github.com/karinaibr/qa-automation-framework.git
cd qa-automation-framework
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Run tests in headless mode:

```bash
pytest --headless
```

Generate Allure results locally:

```bash
pytest --alluredir=allure-results
```

Generate and open the Allure report:

```bash
allure generate allure-results -o allure-report --clean
allure open allure-report
```

## Run Specific Test Areas

Run login tests:

```bash
pytest tests/login -v
```

Run inventory tests:

```bash
pytest tests/inventory -v
```

Run cart tests:

```bash
pytest tests/cart -v
```

## Framework Notes

- Page Objects keep UI interaction logic separate from test assertions.
- `BasePage` contains shared browser interaction behavior such as waits, clicks, and visibility checks.
- `driver_factory.py` centralizes browser creation and headless configuration.
- `conftest.py` manages browser fixtures, pytest hooks, failure screenshots, HTML report paths, and Allure environment data.
- Tests verify visible user behavior and state changes, not only element presence.

## CI/CD and Reporting

GitHub Actions runs the UI test suite automatically on push and pull requests.

The workflow runs tests in headless mode, generates Allure results, builds an Allure report, uploads the report as an artifact for debugging, and publishes the latest report to GitHub Pages.

Failure screenshots are attached to Allure when a test fails.

The latest published report is available here:

[Open UI Allure Report](https://karinaibr.github.io/qa-automation-framework/)

## Next Steps

- Add selected negative UI scenarios where they improve coverage
- Continue improving test stability and reporting details
- Keep README, Allure reports, and project documentation aligned with the current framework state