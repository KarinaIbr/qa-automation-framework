import allure
from pages.login_page import LoginPage


@allure.title("Cart is empty after login")
def test_cart_empty_after_login(driver):
    inventory_page = LoginPage(driver).login("standard_user", "secret_sauce")
    assert not inventory_page.is_shopping_cart_badge_visible()
