import allure
from pages.login_page import LoginPage


@allure.title("Locked out user cannot log in")
def test_locked_out_user_cannot_log_in(driver):
    login_page = LoginPage(driver)

    login_page.attempt_login("locked_out_user", "secret_sauce")
    assert "inventory.html" not in driver.current_url, (
        f"Expected to stay on the login page, but current URL is: {driver.current_url}"
    )
    assert login_page.is_error_message_visible(), "Error message is not visible on login page"
    actual_error = login_page.get_error_message_text()

    assert "Sorry, this user has been locked out" in actual_error, (
        f"Expected locked out message, but got: '{actual_error}'"
    )
