from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TicketRegisterPage:
    URL = 'http://127.0.0.1:5000/register'

    # Locator attributes
    USERNAME = (By.ID, "username")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    CONFIRM_PASSWORD = (By.ID, "confirm_password")
    ACCEPT = (By.ID, "accept")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def register(self, un, em, pw, cfpw):
        # * operator expands self.SEARCH_INPUT into positional arguments for the method call
        username = self.browser.find_element(*self.USERNAME)
        username.send_keys(un + Keys.RETURN)

        email = self.browser.find_element(*self.EMAIL)
        email.send_keys(em + Keys.RETURN)

        password = self.browser.find_element(*self.PASSWORD)
        password.send_keys(pw + Keys.RETURN)

        confirm_password = self.browser.find_element(*self.CONFIRM_PASSWORD)
        confirm_password.send_keys(cfpw + Keys.RETURN)

        accept = self.browser.find_element(*self.ACCEPT)
        accept.send_keys(Keys.SPACE + Keys.TAB + Keys.RETURN)
