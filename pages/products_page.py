"""Page object for the Products (inventory) page and the product details page.

The product details page is small, so its actions live here as well rather
than in a separate file.
"""
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage, product_slug


class ProductsPage(BasePage):
    PAGE_TITLE = (By.CSS_SELECTOR, ".title")
    PRODUCT_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    PRODUCT_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")
    PRODUCT_IMAGES = (By.CSS_SELECTOR, ".inventory_item_img img")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")

    # Product details page
    DETAILS_NAME = (By.CSS_SELECTOR, ".inventory_details_name")
    DETAILS_PRICE = (By.CSS_SELECTOR, ".inventory_details_price")
    BACK_TO_PRODUCTS = (By.ID, "back-to-products")

    # ---- Products listing ----
    def is_products_page_displayed(self):
        return self.is_visible(self.PAGE_TITLE) and self.get_text(self.PAGE_TITLE) == "Products"

    def get_product_names(self):
        return [el.text for el in self.find_all_present(self.PRODUCT_NAMES)]

    def get_product_prices(self):
        return [el.text for el in self.find_all_present(self.PRODUCT_PRICES)]

    def get_product_count(self):
        return len(self.find_all_present(self.PRODUCT_NAMES))

    def get_image_count(self):
        return len(self.find_all_present(self.PRODUCT_IMAGES))

    def add_product_to_cart(self, product_name):
        self.click((By.ID, f"add-to-cart-{product_slug(product_name)}"))

    def remove_product_from_listing(self, product_name):
        self.click((By.ID, f"remove-{product_slug(product_name)}"))

    def get_cart_count(self):
        """Number shown on the cart badge; 0 when the badge is not displayed."""
        try:
            badge = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located(self.CART_BADGE)
            )
            return int(badge.text)
        except TimeoutException:
            return 0

    def open_cart(self):
        self.click(self.CART_LINK)

    def logout(self):
        self.click(self.MENU_BUTTON)
        self.click(self.LOGOUT_LINK)

    # ---- Product details ----
    def open_product_details(self, product_name):
        # XPath is used here because we must find a link by its visible text,
        # which CSS selectors cannot do.
        locator = (
            By.XPATH,
            f"//div[contains(@class,'inventory_item_name') and text()='{product_name}']",
        )
        self.click(locator)

    def get_details_name(self):
        return self.get_text(self.DETAILS_NAME)

    def get_details_price(self):
        return self.get_text(self.DETAILS_PRICE)

    def back_to_products(self):
        self.click(self.BACK_TO_PRODUCTS)
