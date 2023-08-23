from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# -----Locators-----
SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
ORDERS_BUTTON = (By.ID, 'nav-orders')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem')
SIGN_IN_POPUP = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')
BEST_SELLER_LINKS = (By.CSS_SELECTOR, '#zg_header a')
CS_HEADER = (By.CSS_SELECTOR, 'h1[class="fs-heading bolded"]')
CS_DIRECTORY_LINKS = (By.CSS_SELECTOR, '.fs-match-card-title.full')
CS_TEXT_HEADER = (By.CSS_SELECTOR, 'h2[class="fs-heading bolded"]') #'Search our help library' and 'All help topics' headers
CS_SEARCH_BAR = (By.ID, 'hubHelpSearchInput')
CS_TOPICS_COLUMN = (By.CSS_SELECTOR, '[for*="foresight-help-topic"]')


# -----steps-----
@given('Open Amazon BestSellers page')
def open_best_sellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify 5 links display')
def verify_best_seller_links(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.visibility_of_all_elements_located(BEST_SELLER_LINKS))  # Wait for Page Load
    best_seller_links = context.driver.find_elements(*BEST_SELLER_LINKS)
    assert len(best_seller_links) == 5, f'Expected 5 elements but only found {len(best_seller_links)}'


@given('Open Amazon Customer Service page')
def open_customer_service(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()


@then('Verify UI elements')
def verify_cs_elements(context):
    # verify locators can be found
    context.driver.find_element(*CS_HEADER)
    context.driver.find_element(*CS_SEARCH_BAR)

    # verify the search and topics headers both appear (using the same CSS selector to locate, but there should be 2)
    cs_text_header = context.driver.find_elements(*CS_TEXT_HEADER)
    assert len(cs_text_header) == 2, f'Expected 2 elements but only found {len(cs_text_header)}'

    # verify there are 11 directory links on the page
    cs_directory_links = context.driver.find_elements(*CS_DIRECTORY_LINKS)
    assert len(cs_directory_links) == 11, f'Expected 11 elements but only found {len(cs_directory_links)}'

    # verify there are 11 help topic links on the page
    cs_topic_links = context.driver.find_elements(*CS_TOPICS_COLUMN)
    assert len(cs_topic_links) == 11, f'Expected 11 elements but only found {len(cs_topic_links)}'


@when('Search for {search_word}')
def search_on_amazon(context, search_word):
    # context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    # context.driver.find_element(*SEARCH_BUTTON).click()
    context.app.header.search_product(product)


# from HW3
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
    # find_elements will always pass, if there is not a match to the locator it will always pass an empty list,
    # so we need to add an assertion as below
    assert len(links) > 1


@when('Click on button from Sign In popup')
def click_signing_from_popup(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGN_IN_POPUP),
        message='Sign In button pop up not clickable'
    ).click()
    # breaking code like this makes it easier to read


# @then('Verify Sign In page opened')

@when('Click Returns & Orders')
def click_returns_and_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.ID, 'nav-cart').click()
