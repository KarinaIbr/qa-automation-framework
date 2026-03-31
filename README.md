# QA Automation Framework

A UI test automation framework for Swag Labs built with Python, Selenium, and pytest.

The project focuses on clean architecture, maintainable Page Objects, reliable test flows, and clear reporting through Allure, GitHub Actions, and GitHub Pages.

## Live Report

[View the latest Allure Report](https://karinaibr.github.io/qa-automation-framework/)

## Key Features

- Page Object Model with clear separation of concerns
- Structured and maintainable test design
- Cross-browser execution
- Headless test execution
- Allure reporting
- Automatic screenshots on failure
- GitHub Actions CI/CD
- Live Allure Report published via GitHub Pages

## Tech Stack

- Python
- Selenium
- pytest
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

## Covered Scenarios

### Login
- Successful login
- Invalid credentials validation
- Empty field validation

### Inventory
- Inventory page loaded
- Open first product
- Back to products navigation
- Sorting by price: low to high

### Cart
- Add to cart updates button state and cart badge
- Remove from cart updates button state and cart badge
- Product appears in cart with correct details

## How to Run

```bash
git clone https://github.com/karinaibr/qa-automation-framework.git
cd qa-automation-framework
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

### Run in headless mode

```bash
pytest --headless
```

## CI/CD and Reporting

- GitHub Actions runs the UI test suite automatically on push and pull requests.
- Allure Report is generated during CI and uploaded as an artifact for debugging.
- The latest report is also published to GitHub Pages for browser-based review.
- Failure screenshots are attached to Allure to simplify investigation.
