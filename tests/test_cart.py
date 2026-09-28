"""Shopping cart tests (TC_CART_xx)."""
import pytest

pytestmark = pytest.mark.regression

BACKPACK = "Sauce Labs Backpack"


def test_cart_page_opens(products_page, cart_page):
    products_page.add_product_to_cart(BACKPACK)

    products_page.open_cart()

    assert cart_page.is_cart_page_displayed()
    assert "cart" in cart_page.get_current_url()


def test_cart_shows_selected_product_and_matching_price(products_page, cart_page):
    names = products_page.get_product_names()
    prices = products_page.get_product_prices()
    price_on_listing = prices[names.index(BACKPACK)]
    products_page.add_product_to_cart(BACKPACK)

    products_page.open_cart()

    assert cart_page.get_item_names() == [BACKPACK]
    assert cart_page.get_item_prices() == [price_on_listing]
    assert cart_page.get_item_quantities() == ["1"]


def test_remove_product_from_cart(products_page, cart_page):
    products_page.add_product_to_cart(BACKPACK)
    products_page.open_cart()
    assert cart_page.get_item_names() == [BACKPACK]

    cart_page.remove_product(BACKPACK)

    assert cart_page.is_cart_empty(), "Cart should have no items after removal"


def test_continue_shopping_returns_to_products(products_page, cart_page):
    products_page.open_cart()

    cart_page.continue_shopping()

    assert products_page.is_products_page_displayed()
