"""Login and logout tests (manual test cases TC_LOGIN_xx / TC_LOGOUT_xx)."""
import pytest

from pages.products_page import ProductsPage
from utils.data_reader import get_test_data

# Every test in this file is part of the regression suite.
pytestmark = pytest.mark.regression


@pytest.mark.smoke
def test_valid_login(login_page, driver):
    user = get_test_data("valid_user")

    login_page.login(user["username"], user["password"])

    products_page = ProductsPage(driver)
    assert products_page.is_products_page_displayed(), "Products page should open after login"
    assert "inventory" in products_page.get_current_url()


@pytest.mark.negative
@pytest.mark.parametrize("data_id", ["invalid_username", "invalid_password"])
def test_invalid_credentials_show_error(login_page, data_id):
    data = get_test_data(data_id)

    login_page.login(data["username"], data["password"])

    assert login_page.is_error_displayed(), "An error banner should be shown"
    assert login_page.get_error_message() == data["expected_message"]
    assert "inventory" not in login_page.get_current_url(), "User must stay on the login page"


@pytest.mark.negative
@pytest.mark.validation
@pytest.mark.parametrize("data_id", ["empty_username", "empty_password", "both_empty"])
def test_empty_fields_show_required_message(login_page, data_id):
    data = get_test_data(data_id)

    login_page.login(data["username"], data["password"])

    assert login_page.get_error_message() == data["expected_message"]
    assert "inventory" not in login_page.get_current_url()


@pytest.mark.negative
def test_locked_user_cannot_login(login_page):
    data = get_test_data("locked_user")

    login_page.login(data["username"], data["password"])

    assert login_page.get_error_message() == data["expected_message"]
    assert "inventory" not in login_page.get_current_url()


def test_error_message_can_be_dismissed(login_page):
    login_page.login("", "")
    assert login_page.is_error_displayed()

    login_page.dismiss_error()

    assert login_page.is_error_hidden(), "Error banner should disappear after clicking the X"


@pytest.mark.smoke
def test_logout_returns_to_login_page(products_page, login_page):
    products_page.logout()

    assert login_page.is_login_page_displayed(), "Login page should be shown after logout"
