from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Store original window')
def store_original_window(context):
    context.original_window = context.app.amazon_not_found_page.store_original_window()


@when('Click dog image')
def click_dog_img(context):
    context.app.amazon_not_found_page.click_dog_img()


@when('Switch to new window')
def switch_window(context):
    context.app.amazon_not_found_page.switch_to_new_window()

