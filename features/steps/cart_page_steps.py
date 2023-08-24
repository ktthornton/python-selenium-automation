from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@then("Verify empty cart message displays: {expected_text}")
def verify_empty_cart_msg(context, expected_text):
    # verify Your Amazon Cart is empty message displays
    # context.driver.find_element(By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty')
    context.app.cart_page.verify_empty_cart_msg(expected_text)


@then('Verify {expected_count} item displays in the cart')
def verify_cart_count(context, expected_count):

    # expected_cart_result = '1'
    # actual_cart_result = context.driver.find_element(By.ID, 'nav-cart-count').text
    #
    # assert expected_cart_result == actual_cart_result, f'verify_cart error, expected {expected_cart_result} did not match actual {actual_cart_result}'
    context.app.cart_page.verify_cart(expected_count)


@then('Verify added to cart message displays: {expected_text}')
def verify_added_to_cart(context, expected_text):
# verify message displays that item was added to cart
# context.driver.find_element(By.CSS_SELECTOR, '.a-size-medium-plus.a-color-base.sw-atc-text.a-text-bold')
    context.app.cart_page.verify_added_to_cart(expected_text)