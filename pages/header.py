from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BUTTON = (By.ID, 'nav-search-submit-button')
    SIGN_IN_POPUP = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')
    ORDERS_BTN = (By.ID, 'nav-orders')
    LANG_SELECTION = (By.CSS_SELECTOR, ".icp-nav-flag-us")
    SPANISH_LANG = (By.CSS_SELECTOR, '#nav-flyout-icp [href="#switch-lang=es_US"]')
    DEPT_SELECTION = (By.ID, 'searchDropdownBox')

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BUTTON)

    def click_orders(self):
        self.click(*self.ORDERS_BTN)

    def click_signin_from_popup(self):
        self.wait_for_element_clickable_click(self.SIGN_IN_POPUP)

    def verify_signin_btn_clickable(self):
        self.wait_for_element_clickable(self.SIGN_IN_POPUP)

    def verify_signin_btn_disappears(self):
        self.wait_for_element_disappear(self.SIGN_IN_POPUP)

    def hover_language(self):
        actions = ActionChains(self.driver)
        lang = self.find_element(*self.LANG_SELECTION)
        actions.move_to_element(lang)
        actions.perform()

    def verify_spanish_lan(self):
        self.wait_for_element_appear(self.SPANISH_LANG)

    def select_dept(self, dept):
        dept_selection = self.find_element(*self.DEPT_SELECTION)
        select = Select(dept_selection)
        select.select_by_value(f'search-alias={dept}')
