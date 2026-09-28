"""Product listing, product details and add/remove tests (TC_PROD_xx)."""
import pytest

pytestmark = pytest.mark.regression

BACKPACK = "Sauce Labs Backpack"
BIKE_LIGHT = "Sauce Labs Bike Light"
BOLT_TSHIRT = "Sauce Labs Bolt T-Shirt"

# The SauceDemo catalogue contains 6 products for the standard user.
EXPECTED_PRODUCT_COUNT = 6


@pytest.mark.smoke
def test_products_page_loads_after_login(products_page):
    assert products_page.is_products_page_displayed()
    assert "inventory" in products_page.get_current_url()


def test_all_products_are_displayed_with_name_price_and_image(products_page):
    names = products_page.get_product_names()
    prices = products_page.get_product_prices()

    assert len(names) == EXPECTED_PRODUCT_COUNT
    assert len(prices) == EXPECTED_PRODUCT_COUNT
    assert all(name.strip() for name in names), "Every product needs a visible name"
    assert all(price.startswith("$") for price in prices), "Every price should be in dollars"
    assert products_page.get_image_count() == EXPECTED_PRODUCT_COUNT


def test_product_details_match_listing(products_page):
    names = products_page.get_product_names()
    prices = products_page.get_product_prices()
    expected_name, expected_price = names[0], prices[0]

    products_page.open_product_details(expected_name)

    assert products_page.get_details_name() == expected_name
    assert products_page.get_details_price() == expected_price


def test_back_to_products_from_details(products_page):
    products_page.open_product_details(BACKPACK)

    products_page.back_to_products()

    assert products_page.is_products_page_displayed()


@pytest.mark.smoke
def test_add_product_updates_cart_count(products_page):
    products_page.add_product_to_cart(BACKPACK)

    assert products_page.get_cart_count() == 1


def test_add_multiple_products_updates_cart_count(products_page):
    for product in (BACKPACK, BIKE_LIGHT, BOLT_TSHIRT):
        products_page.add_product_to_cart(product)

    assert products_page.get_cart_count() == 3


def test_remove_product_from_listing_updates_cart_count(products_page):
    products_page.add_product_to_cart(BACKPACK)
    products_page.add_product_to_cart(BIKE_LIGHT)
    assert products_page.get_cart_count() == 2

    products_page.remove_product_from_listing(BACKPACK)

    assert products_page.get_cart_count() == 1
