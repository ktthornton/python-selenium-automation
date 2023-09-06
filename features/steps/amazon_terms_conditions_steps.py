from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PRIVACY_NOTICE_HEADER = (By.ID, 'GUID-8966E75F-9B92-4A2B-BFD5-967D57513A40__GUID-2C1DF364-8FA3-4387-BCDB-2A63B7C51B64')


@given('Open Amazon T&C page')
def open_terms_conditions(context):
    context.app.amazon_terms_conditions_page.open_terms_conditions()


@when('Store original windows')
def store_original_windows(context):
    context.original_window = context.app.amazon_terms_conditions_page.get_current_window()


@when('Click on Amazon Privacy Notice link')
def click_privacy_notice(context):
    context.app.amazon_terms_conditions_page.click_privacy_notice()


@when('Switch to the newly opened window')
def switch_windows(context):
    context.app.amazon_terms_conditions_page.switch_to_new_window()
    sleep(2)


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice_opened(context):
    context.app.amazon_terms_conditions_page.verify_partial_url('amazon.com/gp/help/customer/'
                                                                'display.html?nodeId=GX7NJQ4ZB8MHFRNJ')


@then('User can close new window and switch back to original')
def verify_close_window(context):
    context.app.amazon_terms_conditions_page.close_page()
    context.app.amazon_terms_conditions_page.switch_to_window(context.original_window)
    sleep(2)

