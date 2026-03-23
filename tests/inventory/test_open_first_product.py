from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_open_first_product(driver):
    login_page = LoginPage(driver)
    inventory_page = login_page.login("standard_user", "secret_sauce")

    # Capture expected product BEFORE navigation
    expected_title = inventory_page.get_first_product_title()

    # Navigate to product details page
    inventory_page.open_first_product()
    product_page = ProductPage(driver)

    # Verify navigation to product page
    assert product_page.is_back_to_products_visible(), "Back to Products button is not visible on Product page"

    # Verify correct product opened
    actual_title = product_page.get_product_title()
    assert expected_title == actual_title, f"Expected '{expected_title}', but got '{actual_title}'"



