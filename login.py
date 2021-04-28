from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TicketLoginPage:
    URL = 'http://127.0.0.1:5000/login'

    # Locator attributes
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")

    def __init__(self, browser):
        self.browser = browser

    def load(self):  # Navigates browser to login page.
        self.browser.get(self.URL)

    def login(self, un, pw):
        # * operator expands self.SEARCH_INPUT into positional arguments for the method call
        username = self.browser.find_element(*self.USERNAME)
        username.send_keys(un + Keys.RETURN)

        password = self.browser.find_element(*self.PASSWORD)
        password.send_keys(pw + Keys.RETURN)
