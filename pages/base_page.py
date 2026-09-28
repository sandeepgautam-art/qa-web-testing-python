"""BasePage: reusable Selenium actions shared by every page object.

All waiting is done with explicit waits (WebDriverWait + expected
conditions) instead of time.sleep(), so a test waits only as long as needed
and fails with a clear TimeoutException if the page never gets ready.
"""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils import config_reader


def product_slug(product_name):
    """'Sauce Labs Backpack' -> 'sauce-labs-backpack'.

    SauceDemo builds its button ids from the product name in this format,
    e.g. add-to-cart-sauce-labs-backpack.
    """
    return product_name.lower().replace(" ", "-")


class BasePage:
    def __init__(self, driver, timeout=None):
        self.driver = driver
        self.timeout = timeout or config_reader.get_timeout()
        self.wait = WebDriverWait(driver, self.timeout)

    def find_visible(self, locator):
        """Wait until the element is visible, then return it."""
        return self.wait.until(EC.visibility_of_element_located(locator))

    def find_all_present(self, locator):
        """Wait until at least one matching element exists, return all of them."""
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type_text(self, locator, text):
        """Clear the field and type text (an empty string leaves it empty)."""
        element = self.find_visible(locator)
        element.clear()
        if text:
            element.send_keys(text)

    def get_text(self, locator):
        return self.find_visible(locator).text

    def is_visible(self, locator, timeout=None):
        """True if the element becomes visible within the timeout, else False."""
        try:
            WebDriverWait(self.driver, timeout or self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def get_current_url(self):
        return self.driver.current_url
