from pages.login_page import LoginPage
import allure


@allure.title("Sort products by price from low to high")
def test_sorting_price_low_to_high(driver):

    login_page = LoginPage(driver)
    inventory_page = login_page.login("standard_user", "secret_sauce")

    # Capture product prices before sort
    prices_before_sort = inventory_page.get_all_product_prices()

    # Apply price sorting from low to high
    inventory_page.sort_products_by_price_low_to_high()

    # Verify prices are sorted correctly
    prices_after_sort = inventory_page.get_all_product_prices()

    expected_sorted_prices = sorted(prices_before_sort)

    assert expected_sorted_prices == prices_after_sort, (
        f"Expected prices sorted low to high '{expected_sorted_prices}',"
        f" got '{prices_after_sort}'"
    )



