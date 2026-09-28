"""Page object for the SauceDemo login page."""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    ERROR_CLOSE_BUTTON = (By.CSS_SELECTOR, "[data-test='error-button']")

    def open(self, base_url):
        self.driver.get(base_url)
        return self

    def login(self, username, password):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_MESSAGE)

    def is_error_displayed(self):
        return self.is_visible(self.ERROR_MESSAGE)

    def dismiss_error(self):
        self.click(self.ERROR_CLOSE_BUTTON)

    def is_error_hidden(self):
        """True once the error banner has disappeared."""
        return bool(self.wait.until(EC.invisibility_of_element_located(self.ERROR_MESSAGE)))

    def is_login_page_displayed(self):
        return self.is_visible(self.LOGIN_BUTTON)
