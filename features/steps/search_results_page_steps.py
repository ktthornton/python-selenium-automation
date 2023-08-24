from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# -----Locators-----
# SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
# SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
# PRODUCT_NAME = (By.CSS_SELECTOR, '.a-size-base-plus.a-color-base.a-text-normal')
# PRODUCT_IMG = (By.CSS_SELECTOR, '.s-image[data-image-latency="s-product-image"]')
# PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
# PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2 span.a-text-normal')


# -----steps-----
@then('Verify search result is {expected_result}')
def verify_search_result(context, expected_result):
    context.app.search_result_page.verify_search_result(expected_result)


@when('Click on the first product')
def click_first_product(context):
    # context.driver.find_element(*PRODUCT_PRICE).click()
    # sleep(2)
    context.app.search_result_page.click_first_product()


@then('Verify results have a product name and image')
def verify_results_name_img(context):
    # all_products = context.driver.find_elements(*SEARCH_RESULTS)
    #
    # for product in all_products:
    #     product_title = product.find_element(*PRODUCT_TITLE).text
    #     print(product_title)
    #     assert product_title, 'Product title not shown'
    #     product.find_element(*PRODUCT_IMG)
    context.app.search_result_page.verify_results_name_img()
