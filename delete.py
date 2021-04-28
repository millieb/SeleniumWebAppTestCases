from selenium.webdriver.common.keys import Keys
import time


class TicketDeletePage:
    URL = 'http://127.0.0.1:5000/tickets'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def delete_ticket(self, tl):
        # * operator expands self.SEARCH_INPUT into positional arguments for the method call
        title = self.browser.find_element_by_link_text(tl)
        title.send_keys(Keys.TAB + Keys.TAB + Keys.RETURN)
        time.sleep(3)

