from pages.login_page import LoginPage


def test_product_appears_in_cart_with_correct_details(driver):

    login_page = LoginPage(driver)
    inventory_page = login_page.login("standard_user", "secret_sauce")

    # Capture source product data on inventory page
    backpack_name = inventory_page.get_backpack_name()
    backpack_price = inventory_page.get_backpack_price()

    # Add product to cart and open cart page
    inventory_page.click_add_to_cart_backpack_button()
    cart_page = inventory_page.open_cart()

    # Verify cart page state and product details
    page_title = cart_page.get_cart_page_title()
    item_count = cart_page.get_cart_item_count()
    item_name = cart_page.get_cart_item_name()
    item_price = cart_page.get_cart_item_price()

    assert "Your Cart" == page_title, f"Expected cart page title 'Your Cart', got '{page_title}'"
    assert 1 == item_count, f"Expected item count 1, got '{item_count}'"
    assert backpack_name == item_name, f"Expected backpack name '{backpack_name}', got '{item_name}'"
    assert backpack_price == item_price, f"Expected backpack price '{backpack_price}', got '{item_price}'"

