from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open Amazon BestSellers page')
def open_best_sellers(context):
    # context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    context.app.best_seller_page.open_best_sellers()


@then('Verify 5 links display')
def verify_best_seller_links(context):
    # wait = WebDriverWait(context.driver, 10)
    # wait.until(EC.visibility_of_all_elements_located(BEST_SELLER_LINKS))  # Wait for Page Load
    # best_seller_links = context.driver.find_elements(*BEST_SELLER_LINKS)
    # assert len(best_seller_links) == 5, f'Expected 5 elements but only found {len(best_seller_links)}'
    context.app.best_seller_page.verify_best_seller_links()


# @then('User can click through menu links')
