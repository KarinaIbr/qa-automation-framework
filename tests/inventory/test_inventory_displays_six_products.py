from pages.login_page import LoginPage
import allure


@allure.title("Inventory page displays six products")
def test_inventory_displays_six_products(driver):
    login_page = LoginPage(driver)
    inventory_page = login_page.login("standard_user", "secret_sauce")

    expected_products_count = 6
    actual_products_count = inventory_page.get_inventory_items_count()

    assert actual_products_count == expected_products_count, (
        f"Expected {expected_products_count} products, got {actual_products_count}"
    )