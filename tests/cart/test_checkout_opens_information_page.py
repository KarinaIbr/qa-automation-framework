import allure
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage


@allure.title("Checkout opens information page")
def test_checkout_opens_information_page(driver):
    login_page = LoginPage(driver)
    inventory_page = login_page.login("standard_user", "secret_sauce")

    inventory_page.click_add_to_cart_backpack_button()
    cart_page = inventory_page.open_cart()

    checkout_page = cart_page.click_checkout()

    assert checkout_page.is_loaded(), "Checkout information page was not loaded."
