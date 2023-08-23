from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#-----Locators-----
SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
SEARCH_RESULTS = (By.CSS_SELECTOR, '.sg-col-4-of-24.sg-col-4-of-12.s-result-item.s-asin sg-col-4-of-16.AdHolder.sg-col.s-widget-spacing-small.sg-col-4-of-20')
PRODUCT_NAME = (By.CSS_SELECTOR, '.a-size-base-plus.a-color-base.a-text-normal')
PRODUCT_IMG = (By.CSS_SELECTOR, '.s-image[data-image-latency="s-product-image"]')


#-----steps-----
@then('Verify search result is {expected_result}')
def verify_search_result(context, expected_result):
    context.app.search_result_page.verify_search_result(expected_result)

@then('Verify results have a product name and image') #need to get Lana's code for this
def verify_results_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    print(all_products)

    for product in all_products:
        product_title = product.find_element(*PRODUCT_NAME).text()
        assert product_title, 'Product title not shown'
        product.find_element(*PRODUCT_IMG)
