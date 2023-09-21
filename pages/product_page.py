from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class ProductPage(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    PRODUCT_NAME = (By.ID, 'productTitle')
    COLOR_OPTIONS = (By.ID, "inline-twister-expanded-dimension-text-color_name li")
    CURRENT_COLOR = (By.ID, "inline-twister-expanded-dimension-text-color_name .selection")
    COFFEE_PRODUCT = (By.CSS_SELECTOR, '[alt*="Maxwell House Original Medium Roast Ground Coffee"]')
    ONE_TIME_PURCHASE = (By.ID, 'newAccordionRow_0')
    NEW_ARRIVALS = (By.CSS_SELECTOR, '.nav-a.nav-hasArrow[aria-label*="New Arrivals"]')
    NEW_ARRIVALS_MENU = (By.CSS_SELECTOR, '.nav-fullWidthSubnavFlyout.nav-flyout')

    def open_amazon_product(self, product_id):
        self.driver.get(f'https://www.amazon.com/dp/{product_id}/')
        sleep(2)
        self.driver.refresh()

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

    def hover_menu_new_arrivals(self):
        actions = ActionChains(self.driver)
        menu_selection = self.find_element(*self.NEW_ARRIVALS)
        actions.move_to_element(menu_selection)
        actions.perform()
        sleep(3)

    def verify_new_arrivals_menu(self):
        self.wait_for_element_appear(self.NEW_ARRIVALS_MENU)
