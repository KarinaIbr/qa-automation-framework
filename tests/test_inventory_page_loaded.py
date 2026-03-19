from pages.login_page import LoginPage

def test_inventory_page_loaded(driver):
    login_page = LoginPage(driver)
    inventory_page = login_page.login("standard_user", "secret_sauce")

    assert inventory_page.is_products_title_visible(), "Products title is not visible on Inventory page"
    assert inventory_page.get_inventory_items_count() > 0, "Inventory items list is empty"

