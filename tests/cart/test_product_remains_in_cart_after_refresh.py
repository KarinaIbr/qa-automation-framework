import allure
from pages.login_page import LoginPage


@allure.title("Product remains in cart after page refresh")
def test_product_remains_in_cart_after_page_refresh(driver):
    login_page = LoginPage(driver)
    inventory_page = login_page.login("standard_user", "secret_sauce")

    inventory_page.click_add_to_cart_backpack_button()

    actual_button_text = inventory_page.get_remove_backpack_text()
    assert "Remove" == actual_button_text, f"Expected 'Remove', got '{actual_button_text}'"

    driver.refresh()

    actual_button_text_after_refresh = inventory_page.get_remove_backpack_text()
    assert "Remove" == actual_button_text_after_refresh, (
        f"Expected 'Remove' after page refresh, got '{actual_button_text_after_refresh}'"
    )

    badge_visible_after_refresh = inventory_page.is_shopping_cart_badge_visible()
    assert badge_visible_after_refresh, "Shopping cart badge should be visible after refresh"

    actual_badge_text_after_refresh = inventory_page.get_shopping_cart_badge_text()
    assert "1" == actual_badge_text_after_refresh, (
        f"Expected cart badge to show '1' after refresh, got '{actual_badge_text_after_refresh}'"
    )