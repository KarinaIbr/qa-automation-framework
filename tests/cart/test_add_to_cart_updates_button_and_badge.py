from pages.login_page import LoginPage
import allure


@allure.title("Add to cart updates button text and shopping cart badge")
def test_add_to_cart_updates_button_and_badge(driver):
    login_page = LoginPage(driver)
    inventory_page = login_page.login("standard_user", "secret_sauce")

    # Check BEFORE click "Add to cart"
    expected_button_text = inventory_page.get_backpack_button_text()
    assert "Add to cart" == expected_button_text, f"Expected 'Add to cart', got '{expected_button_text}'"

    badge_visible = inventory_page.is_shopping_cart_badge_visible()
    assert not badge_visible, "Shopping cart badge should not be visible before click"

    # Click "Add to cart" button
    inventory_page.click_add_to_cart_backpack_button()

    # Check AFTER click "Add to cart"
    actual_button_text = inventory_page.get_remove_backpack_text()
    assert "Remove" == actual_button_text, f"Expected 'Remove', got '{actual_button_text}'"

    assert inventory_page.is_shopping_cart_badge_visible(), "Shopping cart badge should be visible after click"

    actual_badge_text = inventory_page.get_shopping_cart_badge_text()
    assert "1" == actual_badge_text, f"Expected '1', got '{actual_badge_text}'"

