from behave import given, when, then
from selenium.webdriver.common.by import By


#-----Locators-----
SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
ORDERS_BUTTON = (By.ID, 'nav-orders')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem')


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


@then('Verify footer has {expected_amount} links')
def verify_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*FOOTER_LINKS)
    # print(links)
    print(f'Total links {len(links)}')
    assert len(links) == expected_amount, f'Expected {expected_amount} links, but got {len(links)}'


@then('Verify many links are shown in the footer')
def verify_many_links(context):
    links = context.driver.find_elements(*FOOTER_LINKS)
    #find_elements will always pass, if there is not a match to the locator it will always pass an empty list, so we need to add an assertion as below
    assert len(links) > 1