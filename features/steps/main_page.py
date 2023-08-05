from behave import given, when, then
from selenium.webdriver.common.by import By


#-----Locators-----
SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
ORDERS_BUTTON = (By.ID, 'nav-orders')

#-----steps-----
@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Search for {search_word}')
def search_on_amazon(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BUTTON).click()


#from HW3
# @when('Click Returns & Orders')
# def click_returns_and_orders(context):
#     context.driver.find_element(*ORDERS_BUTTON).click()