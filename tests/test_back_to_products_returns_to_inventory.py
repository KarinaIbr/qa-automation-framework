from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.inventory_page import InventoryPage

def test_back_to_products_returns_to_inventory(driver):

    # Open product page from inventory
    login_page = LoginPage(driver)
    inventory_page = login_page.login("standard_user", "secret_sauce")
    inventory_page.open_first_product()

    # Return back to inventory page
    product_page = ProductPage(driver)
    product_page.click_back_to_products()

    # Re-initialize inventory page after navigation
    inventory_page_after = InventoryPage(driver)

    # Verify user is back on inventory page
    assert inventory_page_after.is_products_title_visible(), "Products title is not visible on Inventory page"
    assert inventory_page_after.get_inventory_items_count() > 0, "Inventory items list is empty"
    assert "inventory.html" in driver.current_url, "User was not redirected to inventory page"

