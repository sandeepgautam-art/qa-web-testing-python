"""Page object for the shopping cart page."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage, product_slug


class CartPage(BasePage):
    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    ITEM_NAMES = (By.CSS_SELECTOR, ".cart_item .inventory_item_name")
    ITEM_PRICES = (By.CSS_SELECTOR, ".cart_item .inventory_item_price")
    ITEM_QUANTITIES = (By.CSS_SELECTOR, ".cart_item .cart_quantity")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    def is_cart_page_displayed(self):
        return self.is_visible(self.PAGE_TITLE) and self.get_text(self.PAGE_TITLE) == "Your Cart"

    def get_item_names(self):
        return [el.text for el in self.find_all_present(self.ITEM_NAMES)]

    def get_item_prices(self):
        return [el.text for el in self.find_all_present(self.ITEM_PRICES)]

    def get_item_quantities(self):
        return [el.text for el in self.find_all_present(self.ITEM_QUANTITIES)]

    def remove_product(self, product_name):
        self.click((By.ID, f"remove-{product_slug(product_name)}"))

    def is_cart_empty(self):
        """Wait for the item rows to disappear; True when the cart has no items."""
        return bool(self.wait.until(EC.invisibility_of_element_located(self.CART_ITEMS)))

    def checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)
