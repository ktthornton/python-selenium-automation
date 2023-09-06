from pages.base_page import Page
from selenium.webdriver.common.by import By


class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty')
    ITM_ADDED_TO_CART = (By.CSS_SELECTOR, '.a-size-medium-plus.a-color-base.sw-atc-text.a-text-bold')
    CART_COUNT = (By.ID, 'nav-cart-count')

    def verify_empty_cart_msg(self, expected_text):
        actual_text = self.find_element(*self.CART_EMPTY_MSG).text
        assert actual_text == expected_text,    \
            f'Error, expected {expected_text} did not match actual {actual_text}'

    def verify_cart(self, expected_count):
        actual_count = self.find_element(*self.CART_COUNT).text
        assert actual_count == expected_count,  \
            f'Error, expected {expected_count} items but found {actual_count}'

    def verify_added_to_cart(self, expected_text):
        actual_text = self.find_element(*self.ITM_ADDED_TO_CART).text
        assert actual_text == expected_text, \
            f'Error, expected {expected_text} did not match actual {actual_text}'
