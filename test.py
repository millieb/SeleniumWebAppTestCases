import pytest
from selenium import webdriver
from edit import TicketEditPage
from login import TicketLoginPage
from create import TicketCreatePage
from delete import TicketDeletePage
from register import TicketRegisterPage


@pytest.fixture
def browser():
    PATH = r"C:\WebDriver\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.implicitly_wait(15)
    yield driver  # return driver object at the end of the setup
    driver.quit()


# Test: Correct Login
def test_sign_in(browser):
    USERNAME = 'mildred'
    PASSWORD = 'kira123'

    login_page = TicketLoginPage(browser)
    login_page.load()
    login_page.login(USERNAME, PASSWORD)


# Test: Correct Register
def test_register(browser):
    USERNAME = 'kira'
    EMAIL = 'kira@gmail.com'
    PASSWORD = 'kira123'
    CONFIRM_PASSWORD = 'kira123'

    register_page = TicketRegisterPage(browser)
    register_page.load()
    register_page.register(USERNAME, EMAIL, PASSWORD, CONFIRM_PASSWORD)


# Test: Correct Ticket Creation
def test_create_ticket(browser):
    TITLE = 'Selenium Ticket 5'
    DESCRIPTION = 'Selenium Description 5'

    # Login before creating ticket
    login_page = TicketLoginPage(browser)
    login_page.load()
    login_page.login('mildred', 'kira123')

    create_page = TicketCreatePage(browser)
    create_page.load()
    create_page.create_ticket(TITLE, DESCRIPTION)


# Test: Correct Ticket Edit
def test_edit_ticket(browser):
    NAME = 'Ticket 1'
    TITLE = 'Modified Title'
    DESCRIPTION = 'Modified Description'
    COMPANY = 'OV'
    CATEGORY = 'HW'

    # Login before creating ticket
    login_page = TicketLoginPage(browser)
    login_page.load()
    login_page.login('mildred', 'kira123')

    edit_page = TicketEditPage(browser)
    edit_page.load()
    edit_page.edit_ticket(NAME, TITLE, DESCRIPTION, COMPANY, CATEGORY)


# Test: Correct Ticket Deletion
def test_delete_ticket(browser):
    NAME = 'Ticket 6'

    # Login before creating ticket
    login_page = TicketLoginPage(browser)
    login_page.load()
    login_page.login('mildred', 'kira123')

    delete_page = TicketDeletePage(browser)
    delete_page.load()
    delete_page.delete_ticket(NAME)
