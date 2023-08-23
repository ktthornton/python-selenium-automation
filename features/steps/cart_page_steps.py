from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@then("Verify 'Your Amazon Cart is empty' message displays")
def verify_cart_is_empty(context):
    # verify Your Amazon Cart is empty message displays
    context.driver.find_element(By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty')


@then('Verify the item displays in the cart')
def verify_cart(context):
    # verify message displays that item was added to cart
    context.driver.find_element(By.CSS_SELECTOR, '.a-size-medium-plus.a-color-base.sw-atc-text.a-text-bold')

    expected_cart_result = '1'
    actual_cart_result = context.driver.find_element(By.ID, 'nav-cart-count').text

    assert expected_cart_result == actual_cart_result, f'verify_cart error, expected {expected_cart_result} did not match actual {actual_cart_result}'
