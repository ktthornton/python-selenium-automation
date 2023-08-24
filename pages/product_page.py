from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProductPage(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    PRODUCT_NAME = (By.ID, 'productTitle')
    COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
    CURRENT_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")
    COFFEE_PRODUCT = (By.CSS_SELECTOR, '[alt*="Maxwell House Original Medium Roast Ground Coffee"]')
    ONE_TIME_PURCHASE = (By.ID, 'newAccordionRow_0')

    def open_amazon_product(self, product_id):
        self.driver.get(f'https://www.amazon.com/dp/{product_id}/')

    def click_add_to_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BTN).click()

    def get_product_name(self):
        product_name = self.find_element(*self.PRODUCT_NAME).text
        print(f'Current product: {product_name}')

    def verify_can_click_colors(self, expected_colors):
        colors = self.driver.find_elements(*self.COLOR_OPTIONS)
        actual_colors = []
        for color in colors:
            color.click()
            current_color = self.driver.find_element(*self.CURRENT_COLOR).text
            actual_colors.append(current_color)

        assert actual_colors == expected_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

    def add_to_cart(self):
        self.find_element(*self.COFFEE_PRODUCT).click()
        self.find_element(*self.ONE_TIME_PURCHASE).click()
        # # click on 'One-time purchase' - may need to be removed based on Amazon...
        # # I keep running the test and it oscillates between 'One-time purchase' already is selected instead of
        # # 'Subscribe & Save'.
        self.find_element(*self.ADD_TO_CART_BTN).click()
