from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    SIGN_IN_POPUP = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')
    ORDERS_BTN = (By.ID, 'nav-orders')

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)

    def click_orders(self):
        self.click(*self.ORDERS_BTN)

    def click_signin_from_popup(self):
        self.wait_for_element_clickable_click(*self.SIGN_IN_POPUP)

    def verify_signin_btn_clickable(self):
        self.wait_for_element_clickable(*self.SIGN_IN_POPUP)

    def verify_signin_btn_disappears(self):
        self.wait_for_element_disappear(*self.SIGN_IN_POPUP)
