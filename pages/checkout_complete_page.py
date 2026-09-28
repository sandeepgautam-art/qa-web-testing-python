"""Page object for the order confirmation page."""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutCompletePage(BasePage):
    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    CONFIRMATION_HEADER = (By.CSS_SELECTOR, ".complete-header")
    CONFIRMATION_TEXT = (By.CSS_SELECTOR, ".complete-text")
    BACK_HOME_BUTTON = (By.ID, "back-to-products")

    def is_order_confirmation_displayed(self):
        return self.is_visible(self.CONFIRMATION_HEADER)

    def get_confirmation_header(self):
        return self.get_text(self.CONFIRMATION_HEADER)

    def get_confirmation_text(self):
        return self.get_text(self.CONFIRMATION_TEXT)

    def back_to_products(self):
        self.click(self.BACK_HOME_BUTTON)
