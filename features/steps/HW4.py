from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, then


#-----locators-----
BEST_SELLER_LINKS = (By.CSS_SELECTOR, '[class*="_p13n-zg-nav-tab-all_style_zg-tabs-li"]')
CS_HEADER = (By.CSS_SELECTOR, 'h1[class="fs-heading bolded"]')
CS_DIRECTORY_LINKS = (By.CSS_SELECTOR, '.fs-match-card-title.full')
CS_TEXT_HEADER = (By.CSS_SELECTOR, 'h2[class="fs-heading bolded"]') #'Search our help library' and 'All help topics' headers
CS_SEARCH_BAR = (By.ID, 'hubHelpSearchInput')
CS_TOPICS_COLUMN = (By.CSS_SELECTOR, '[for*="foresight-help-topic"]')


#-----test scenarios-----

#scenario 1/HW problem 1
@given('Open Amazon BestSellers page')
def open_best_sellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify 5 links display')
def verify_best_seller_links(context):
    wait = WebDriverWait(context.driver, 10)
    wait.until(EC.visibility_of_all_elements_located(BEST_SELLER_LINKS))  # Wait for Page Load
    best_seller_links = context.driver.find_elements(*BEST_SELLER_LINKS)
    assert len(best_seller_links) == 5


#scenario 2/HW problem 3
@given('Open Amazon Customer Service page')
def open_customer_service(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')


@then('Verify UI elements')
def verify_cs_elements(context):
    #verify locators can be found
    context.driver.find_element(*CS_HEADER)
    context.driver.find_element(*CS_SEARCH_BAR)


    #verify the search and topics  headers both appear (using the same CSS selector to locate, but there should be 2)
    cs_text_header = context.driver.find_elements(*CS_TEXT_HEADER)
    assert len(cs_text_header) == 2

    # verify there are 11 directory links on the page
    cs_directory_links = context.driver.find_elements(*CS_DIRECTORY_LINKS)
    assert len(cs_directory_links) == 11

    # verfiy there are 11 help topic links on the page
    cs_topic_links = context.driver.find_elements(*CS_TOPICS_COLUMN)
    assert len(cs_topic_links) == 11

#-----


# BEST_SELLER_LINKS = (By.CSS_SELECTOR, '[class*="_p13n-zg-nav-tab-all_style_zg-tabs-li"]')


# @given('Open Amazon BestSellers page')
# def open_best_sellers(context):
#     context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
#
#
# @then('Verify 5 links display')
# def verify_best_seller_links(context):
#     sleep(10)
#     # wait = WebDriverWait(context.driver, 10)
#     # wait.until(EC.visibility_of_all_elements_located(BEST_SELLER_LINKS))  # Wait for Page Load
#     best_seller_links = context.driver.find_elements(*BEST_SELLER_LINKS)
#
#     print("Number of links found:", len(best_seller_links))  # Print Debug Information
#     assert len(best_seller_links) == 5
