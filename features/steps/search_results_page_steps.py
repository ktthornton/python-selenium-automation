from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#-----Locators-----
SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
RESULT_NAME = ()
RESULT_IMG = (By.CSS_SELECTOR, 'img[data-image-latency="s-product-image"]')


#-----steps-----
@then('Verify search result is {expected_result}')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(*SEARCH_RESULT).text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'

