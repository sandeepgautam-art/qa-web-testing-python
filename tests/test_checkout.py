"""Checkout and order completion tests (TC_CHK_xx)."""
import pytest

from utils.data_reader import get_test_data

pytestmark = pytest.mark.regression

BACKPACK = "Sauce Labs Backpack"


@pytest.fixture
def on_checkout_page(products_page, cart_page):
    """Logged in, one product in the cart, sitting on checkout step one."""
    products_page.add_product_to_cart(BACKPACK)
    products_page.open_cart()
    cart_page.checkout()


def _money(text):
    """'Item total: $29.99' -> 29.99"""
    return float(text.split("$")[1])


def test_checkout_page_opens(on_checkout_page, checkout_page):
    assert checkout_page.is_information_page_displayed()
    assert "checkout-step-one" in checkout_page.get_current_url()


@pytest.mark.smoke
def test_valid_customer_information_reaches_overview(on_checkout_page, checkout_page):
    data = get_test_data("checkout_valid")

    checkout_page.enter_customer_information(
        data["first_name"], data["last_name"], data["postal_code"]
    )
    checkout_page.continue_to_overview()

    assert checkout_page.is_overview_page_displayed()


@pytest.mark.negative
@pytest.mark.validation
@pytest.mark.parametrize(
    "data_id",
    [
        "checkout_missing_first_name",
        "checkout_missing_last_name",
        "checkout_missing_postal_code",
        "checkout_all_empty",
    ],
)
def test_required_checkout_fields_are_validated(on_checkout_page, checkout_page, data_id):
    data = get_test_data(data_id)

    checkout_page.enter_customer_information(
        data["first_name"], data["last_name"], data["postal_code"]
    )
    checkout_page.continue_to_overview()

    assert checkout_page.get_error_message() == data["expected_message"]
    assert checkout_page.is_information_page_displayed(), "User must not advance with invalid data"


def test_cancel_on_information_page_returns_to_cart(on_checkout_page, checkout_page, cart_page):
    checkout_page.cancel()

    assert cart_page.is_cart_page_displayed()


def test_overview_total_equals_item_total_plus_tax(on_checkout_page, checkout_page):
    data = get_test_data("checkout_valid")
    checkout_page.enter_customer_information(
        data["first_name"], data["last_name"], data["postal_code"]
    )
    checkout_page.continue_to_overview()

    item_total = _money(checkout_page.get_item_total_text())
    tax = _money(checkout_page.get_tax_text())
    total = _money(checkout_page.get_total_text())

    assert round(item_total + tax, 2) == total


@pytest.mark.smoke
def test_complete_order_shows_confirmation(on_checkout_page, checkout_page, checkout_complete_page):
    data = get_test_data("checkout_valid")
    checkout_page.enter_customer_information(
        data["first_name"], data["last_name"], data["postal_code"]
    )
    checkout_page.continue_to_overview()

    checkout_page.finish_checkout()

    assert checkout_complete_page.is_order_confirmation_displayed()
    assert checkout_complete_page.get_confirmation_header() == "Thank you for your order!"
    assert "checkout-complete" in checkout_complete_page.get_current_url()


def test_cart_is_empty_after_order_completion(
    on_checkout_page, checkout_page, checkout_complete_page, products_page
):
    data = get_test_data("checkout_valid")
    checkout_page.enter_customer_information(
        data["first_name"], data["last_name"], data["postal_code"]
    )
    checkout_page.continue_to_overview()
    checkout_page.finish_checkout()

    checkout_complete_page.back_to_products()

    assert products_page.is_products_page_displayed()
    assert products_page.get_cart_count() == 0
