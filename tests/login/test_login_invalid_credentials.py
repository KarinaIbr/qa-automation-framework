import pytest
from pages.login_page import LoginPage
import allure


@allure.title("Login is rejected for invalid credentials ({param_id})")
@pytest.mark.parametrize(
    "username, password",
    [
    ("standard_user", "asd"),
    ("qqqq", "secret_sauce"),
    ("asdfgh", "asdfgh")
    ],
    ids=[
        "valid_user_invalid_password",
        "invalid_user_valid_password",
        "invalid_user_invalid_password"
    ]
)

def test_login_invalid_credentials(driver, username, password):

    # Attempt login with invalid credentials
    login_page = LoginPage(driver)
    login_page.attempt_login(username, password)

    # Verify NO redirect happened
    assert "inventory.html" not in driver.current_url

    # Verify error handling
    assert login_page.is_error_message_visible(), "Error message is not visible on login page"
    assert "do not match any user" in login_page.get_error_message_text(), "Error message text does not match"
