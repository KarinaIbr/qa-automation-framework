from pages.login_page import LoginPage

def test_remove_from_cart_updates_button_and_badge(driver):
    login_page = LoginPage(driver)
    inventory_page = login_page.login("standard_user", "secret_sauce")

    # Creating precondition for remove-test
    inventory_page.click_add_to_cart_backpack_button()

    # Click remove button
    inventory_page.click_remove_backpack_button()

    actual_button_text = inventory_page.get_backpack_button_text()
    assert "Add to cart" == actual_button_text, f"Expected 'Add to cart', got '{actual_button_text}'"

    badge_visible = inventory_page.is_shopping_cart_badge_visible()
    assert not badge_visible, "Shopping cart badge should not be visible after remove"
