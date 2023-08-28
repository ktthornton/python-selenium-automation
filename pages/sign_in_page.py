from pages.base_page import Page
from selenium.webdriver.common.by import By


class SignInPage(Page):
    SIGN_IN_HEADER = (By.CSS_SELECTOR, 'h1[class="a-spacing-small"]')
    EMAIL = (By.ID, 'ap_email')

    def verify_sign_in_page(self):
        self.verify_text('Sign in', *self.SIGN_IN_HEADER)
        self.find_element(*self.EMAIL)
        self.verify_partial_url('ap/signin')


