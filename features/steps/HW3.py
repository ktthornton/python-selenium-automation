#-----Locators-----
#Amazon logo - search by $$(".a-icon a-icon-logo")
#Create account header - search by $$('h1[class=a-spacing-small]')
#Your Name field - search by id="ap_customer_name"
#Email field - search by id="ap_email"
#Password field - search by id="ap_password"
#Password requirement text - search by $$('[class*="  Passwords must be at least 6 characters."]')
#Re-enter password field - search by id="ap_password_check"
#Create your Amazon account button - search by id="continue"
#Conditions of Use link - search by $$('[href*="condition_of_use"]')
#Privacy Notice link - search by $$('[href*="privacy_notice"]')
#Sign in link - search by $$('[class*="signin"]')



#-----Test case script-----
from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


#scenario 1/HW problem 2
@given('Open new Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click Returns & Orders')
def click_returns_and_orders(context):
    context.driver.find_element(By.ID, 'nav-orders').click()


@then('Verify user is brought to Sign In page')
def verify_sign_in_page(context):
    #verfiy Sign in header is visible
    context.driver.find_element(By.CSS_SELECTOR, 'h1[class="a-spacing-small"]')
    #verify email input field is present
    context.driver.find_element(By.ID, 'ap_email')


#scenario 2/HW problem 3
@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.ID, 'nav-cart').click()


@then("Verify 'Your Amazon Cart is empty' message displays")
def verify_cart_is_empty(context):
    #verify Your Amazon Cart is empty message displays
    context.driver.find_element(By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty')


#scenario3/creative
@then('Search for an item')
def amazon_search(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('coffee')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@when('Add item to cart')
def add_to_cart(context):
    #select an item from the results list
    context.driver.find_element(By.CSS_SELECTOR, '[alt*="Maxwell House Original Medium Roast Ground Coffee"]').click()

    #click on 'One-time purchase' - may need to be removed based on Amazon...I keep running the test and it oscillates between 'One-time purchase' already is selected instead of 'Subscribe & Save'.
    context.driver.find_element(By.ID, 'newAccordionRow_0').click()

    #click 'Add to Cart'
    context.driver.find_element(By.ID, 'add-to-cart-button').click()


@then('Verify the item displays in the cart')
def verify_cart(context):
    #verify message displays that item was added to cart
    context.driver.find_element(By.CSS_SELECTOR, '.a-size-medium-plus.a-color-base.sw-atc-text.a-text-bold')

    expected_cart_result = '1'
    actual_cart_result = context.driver.find_element(By.ID, 'nav-cart-count').text

    assert expected_cart_result == actual_cart_result, f'verify_cart error, expected {expected_cart_result} did not match actual {actual_cart_result}'

