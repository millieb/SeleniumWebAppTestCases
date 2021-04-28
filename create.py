import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# noinspection DuplicatedCode
class TicketCreatePage:
    URL = 'http://127.0.0.1:5000/tickets/new'

    # Locator attributes
    TITLE = (By.ID, "title")
    DESCRIPTION = (By.ID, "description")
    CREATE = (By.NAME, "button")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def create_ticket(self, tl, ds):
        # * operator expands self.SEARCH_INPUT into positional arguments for the method call
        title = self.browser.find_element(*self.TITLE)
        title.send_keys(tl + Keys.RETURN)
        time.sleep(3)
        description = self.browser.find_element(*self.DESCRIPTION)
        description.send_keys(ds + Keys.RETURN)
        time.sleep(3)
        create = self.browser.find_element(*self.CREATE)
        create.send_keys(Keys.RETURN)
        time.sleep(2)