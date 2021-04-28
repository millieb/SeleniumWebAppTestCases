import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class TicketEditPage:
    URL = 'http://127.0.0.1:5000/tickets'

    # Locator attributes
    TITLE_TEXTBOX = (By.ID, "title")
    DESCRIPTION_TEXTBOX = (By.ID, "description")
    SAVE_BUTTON = (By.NAME, "button")

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def edit_ticket(self, nm, tltx, dstx, cpcb, ctcb):
        # * operator expands self.SEARCH_INPUT into positional arguments for the method call
        name = self.browser.find_element_by_link_text(nm)
        name.send_keys(Keys.TAB + Keys.RETURN)
        time.sleep(3)
        title = self.browser.find_element(*self.TITLE_TEXTBOX)
        title.send_keys(Keys.TAB + Keys.TAB + Keys.TAB)
        title.clear()
        title.send_keys(tltx)
        time.sleep(2)
        description = self.browser.find_element(*self.DESCRIPTION_TEXTBOX)
        description.clear()
        description.send_keys(dstx + Keys.RETURN)
        time.sleep(2)
        company = Select(self.browser.find_element_by_id("company"))
        company.select_by_value(cpcb)
        time.sleep(2)
        category = Select(self.browser.find_element_by_id("category"))
        category.select_by_value(ctcb)
        time.sleep(2)
        save = self.browser.find_element(*self.SAVE_BUTTON)
        save.click()
        time.sleep(3)
