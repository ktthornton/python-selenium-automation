from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class MainPage(Page):
    FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem')
    SIGN_IN_POPUP = (By.ID, 'nav-signin-tooltip')
    ORDERS_BUTTON = (By.ID, 'nav-orders')
    CART_ICON = (By.ID, 'nav-cart')
    SEARCH_INPUT = (By.NAME, 'q')
    SEARCH_SUBMIT = (By.NAME, 'btnK')
    CUSTOMER_SERVICE = (By.CSS_SELECTOR, 'a[href*="nav_cs_fs_hub_navbar_c"]')

    def open_main(self):
        self.driver.get('https://www.amazon.com/')
        sleep(2)
        self.driver.refresh()

    def open_customer_service(self):
        self.driver.find_element(*self.CUSTOMER_SERVICE).click()

    def verify_footer_link_amount(self, expected_amount):
        expected_amount = int(expected_amount)
        actual_links = self.driver.find_elements(*self.FOOTER_LINKS)
        assert len(actual_links) == expected_amount, f'Expected {expected_amount} links, but got {len(actual_links)}'

    def verify_many_footer_links(self):
        actual_links = self.driver.find_elements(*self.FOOTER_LINKS)
        assert len(actual_links) > 1, f'Only {len(actual_links)} was found'

    def click_signin_from_popup(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.wait.until(EC.element_to_be_clickable(self.SIGN_IN_POPUP),
                               message='Sign In button pop up not clickable'
                               ).click()

    def click_returns_and_orders(self):
        self.driver.find_element(*self.ORDERS_BUTTON).click()

    def click_cart_icon(self):
        self.driver.find_element(*self.CART_ICON).click()

# Google searches
    def open_google(self):
        self.driver.get('https://www.google.com/')

    def input_search(self, search_word):
        search = self.find_element(*self.SEARCH_INPUT)
        search.clear()
        search.send_keys(search_word)

    def click_search_icon(self):
        self.find_element(*self.SEARCH_SUBMIT).click()

    def verify_found_results_text(self, search_word):
        assert search_word.lower() in self.driver.current_url.lower(),\
            f'Expected query not in {self.driver.current_url.lower()}'

