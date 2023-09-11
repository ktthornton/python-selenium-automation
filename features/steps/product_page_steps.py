from selenium.webdriver.common.by import By
from behave import *

# --- Locators ---
# ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
# PRODUCT_NAME = (By.ID, 'productTitle')
COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")


# --- Steps ---
@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    # context.driver.get(f'https://www.amazon.com/dp/{product_id}/')
    context.app.product_page.open_amazon_product(product_id)

@when('Click on Add to cart button')
def click_add_to_cart(context):
    # context.driver.find_element(*ADD_TO_CART_BTN).click()
    # sleep(2)
    context.app.product_page.click_add_to_cart()


@when('Store product name')
def get_product_name(context):
    # context.product_name = context.driver.find_element(*PRODUCT_NAME).text
    # print(f'Current product: {context.product_name}')
    context.app.product_page.get_product_name()


@then('Verify user can click through colors')
def verify_can_click_colors(context):
    expected_colors = ['Bespoke Way (Blue)', 'Black', 'CUPIDS WAY (ROSEMARINE PINK/RED PLUM)', 'Green']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text

        actual_colors.append(current_color)

    assert actual_colors == expected_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
    # context.app.product_page.verify_can_click_colors(
    #     expected_colors=['Bespoke Way (Blue)', 'Black',
    #                      'CUPIDS WAY (ROSEMARINE PINK/RED PLUM)', 'Green'])


@when('Add item to cart')
def add_to_cart(context):
    # select an item from the results list
    # context.driver.find_element(By.CSS_SELECTOR, '[alt*="Maxwell House Original Medium Roast Ground Coffee"]').click()
    #
    # # click on 'One-time purchase' - may need to be removed based on Amazon...
    # # I keep running the test and it oscillates between 'One-time purchase' already is selected instead of
    # # 'Subscribe & Save'.
    # context.driver.find_element(By.ID, 'newAccordionRow_0').click()
    #
    # # click 'Add to Cart'
    # context.driver.find_element(By.ID, 'add-to-cart-button').click()
    context.app.product_page.add_to_cart()


@when('Hover over New Arrivals menu item')
def hover_menu_new_arrivals(context):
    context.app.product_page.hover_menu_new_arrivals()


@then('Verify New Arrivals menu is present')
def verify_new_arrivals_menu(context):
    pass
