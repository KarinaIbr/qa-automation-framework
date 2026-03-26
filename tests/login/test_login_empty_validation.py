import pytest
from pages.login_page import LoginPage
import allure


@allure.title("Login validation works for empty credentials ({param_id})")
@pytest.mark.parametrize(
    "username, password, expected_error_text",
    [
    ("standard_user", "", "Password is required"),
    ("", "secret_sauce", "Username is required"),
    ("", "", "Username is required")
    ],
    ids=[
        "valid_username_empty_password",
        "empty_username_valid_password",
        "empty_username_empty_password"
    ]
)

def test_login_empty_validation(driver, username, password, expected_error_text):

    # Attempt login with empty/invalid input
    login_page = LoginPage(driver)
    login_page.attempt_login(username, password)

    # Verify NO redirect happened
    assert "inventory.html" not in driver.current_url

    # Verify error handling
    assert login_page.is_error_message_visible(), "Error message is not visible on login page"
    assert expected_error_text in login_page.get_error_message_text(), "Error message text does not match"
