import allure
from pages.login_page import LoginPage


@allure.title("Unauthorized user cannot access inventory page")
def test_unauthorized_user_cannot_access_inventory(driver):
    login_page = LoginPage(driver)

    login_page.open("https://www.saucedemo.com/inventory.html")
    assert "inventory.html" not in driver.current_url, (
        f"Expected unauthorized user to be denied access to the inventory page, "
        f"but current URL is: {driver.current_url}"
    )

    assert login_page.is_error_message_visible(), (
        "Expected access denied error message to be visible, but it was not displayed"
    )

