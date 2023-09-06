from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@then('Verify blog is opened')
def verify_blog_opened(context):
    context.app.amazon_blog.verify_opened()


@then('Close blog')
def close_blog(context):
    context.app.amazon_blog.close_page()


@then('Return to original window')
def return_to_original_window(context):
    context.app.amazon_blog.switch_to_window(context.original_window)
