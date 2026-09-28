"""Shared pytest fixtures and hooks for every test file.

Fixtures defined here are discovered automatically by pytest - test files
do not need to import them.
"""
import base64

import pytest

from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils import config_reader
from utils.data_reader import get_test_data
from utils.driver_factory import create_driver
from utils.screenshot import take_screenshot


# --------------------------------------------------------------------------
# Fixtures
# --------------------------------------------------------------------------
@pytest.fixture(scope="session")
def base_url():
    """Application URL, read from config/config.ini."""
    return config_reader.get_base_url()


@pytest.fixture
def driver():
    """Start a fresh browser for each test and always close it afterwards."""
    web_driver = create_driver()
    yield web_driver  # the test runs here
    web_driver.quit()  # teardown - runs even if the test failed


@pytest.fixture
def login_page(driver, base_url):
    """Browser opened on the login page."""
    return LoginPage(driver).open(base_url)


@pytest.fixture
def products_page(login_page, driver):
    """Browser logged in as the standard demo user, on the Products page."""
    user = get_test_data("valid_user")
    login_page.login(user["username"], user["password"])
    page = ProductsPage(driver)
    assert page.is_products_page_displayed(), "Setup failed: login did not reach Products page"
    return page


@pytest.fixture
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture
def checkout_page(driver):
    return CheckoutPage(driver)


@pytest.fixture
def checkout_complete_page(driver):
    return CheckoutCompletePage(driver)


# --------------------------------------------------------------------------
# Screenshot on failure
# --------------------------------------------------------------------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Runs after each test phase. If a test failed, save a screenshot.

    "hookwrapper" lets us wait for pytest to build the normal report
    (yield), then inspect and extend it.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when not in ("setup", "call") or not report.failed:
        return

    web_driver = item.funcargs.get("driver")  # only tests that used the browser
    if web_driver is None:
        return

    try:
        screenshot_path = take_screenshot(web_driver, item.name)
        print(f"\nScreenshot saved: {screenshot_path}")
    except Exception as error:  # noqa: BLE001 - never hide the real test failure
        print(f"\nCould not capture screenshot: {error}")
        return

    # Also embed the screenshot in the pytest-html report (if installed).
    try:
        from pytest_html import extras

        encoded = base64.b64encode(screenshot_path.read_bytes()).decode("utf-8")
        report_extras = getattr(report, "extras", [])
        report_extras.append(extras.png(encoded, name="Screenshot on failure"))
        report.extras = report_extras
    except ImportError:
        pass


# --------------------------------------------------------------------------
# HTML report customisation (pytest-html)
# --------------------------------------------------------------------------
def pytest_html_report_title(report):
    report.title = "Web Application Testing & QA Automation - Test Report"
