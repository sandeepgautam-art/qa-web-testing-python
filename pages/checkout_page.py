"""Page object for both checkout steps.

Step one = customer information form. Step two = order overview.
They are one short flow, so one class keeps things simple.
"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    # Step two (overview)
    FINISH_BUTTON = (By.ID, "finish")
    ITEM_TOTAL = (By.CSS_SELECTOR, ".summary_subtotal_label")
    TAX = (By.CSS_SELECTOR, ".summary_tax_label")
    TOTAL = (By.CSS_SELECTOR, ".summary_total_label")

    # ---- Step one ----
    def is_information_page_displayed(self):
        return (
            self.is_visible(self.PAGE_TITLE)
            and self.get_text(self.PAGE_TITLE) == "Checkout: Your Information"
        )

    def enter_customer_information(self, first_name, last_name, postal_code):
        self.type_text(self.FIRST_NAME_INPUT, first_name)
        self.type_text(self.LAST_NAME_INPUT, last_name)
        self.type_text(self.POSTAL_CODE_INPUT, postal_code)

    def continue_to_overview(self):
        self.click(self.CONTINUE_BUTTON)

    def cancel(self):
        self.click(self.CANCEL_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    # ---- Step two ----
    def is_overview_page_displayed(self):
        return (
            self.is_visible(self.PAGE_TITLE)
            and self.get_text(self.PAGE_TITLE) == "Checkout: Overview"
        )

    def get_item_total_text(self):
        return self.get_text(self.ITEM_TOTAL)

    def get_tax_text(self):
        return self.get_text(self.TAX)

    def get_total_text(self):
        return self.get_text(self.TOTAL)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)
