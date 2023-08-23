from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# -----Locators-----
# Amazon logo - search by $$(".a-icon a-icon-logo")
# Create account header - search by $$('h1[class=a-spacing-small]')
# Your Name field - search by id="ap_customer_name"
# Email field - search by id="ap_email"
# Password field - search by id="ap_password"
# Password requirement text - search by $$('[class*="  Passwords must be at least 6 characters."]')
# Re-enter password field - search by id="ap_password_check"
# Create your Amazon account button - search by id="continue"
# Conditions of Use link - search by $$('[href*="condition_of_use"]')
# Privacy Notice link - search by $$('[href*="privacy_notice"]')
# Sign in link - search by $$('[class*="signin"]')


# -----steps-----
@then('Verify user is brought to Sign In page')
def verify_sign_in_page(context):
    # verify Sign in header is visible
    context.driver.find_element(By.CSS_SELECTOR, 'h1[class="a-spacing-small"]')
    # verify email input field is present
    context.driver.find_element(By.ID, 'ap_email')
