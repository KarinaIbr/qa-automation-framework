from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_login_success(driver):

    #Step 1: Login with valid credentials
    login_page = LoginPage(driver)
    inventory_page = login_page.login("standard_user", "secret_sauce")

    #Step 2: Verify Products title is visible
    assert inventory_page.is_products_title_visible(), "Products title is not visible on Inventory page"

    #Step 3: Optional URL check can be added if needed
    #assert "inventory.html" in driver.current_url, "User was not redirected to inventory page"

