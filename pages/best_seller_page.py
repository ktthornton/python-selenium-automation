from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BestSellerPage(Page):
    BEST_SELLER_LINKS = (By.CSS_SELECTOR, '#zg_header a')
    # MENU_LINKS = #need to get from Lana's code
    # HEADER = #need to get from Lana's code

    def open_best_sellers(self):
        self.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

    def verify_best_seller_links(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.wait.until(EC.visibility_of_all_elements_located(self.BEST_SELLER_LINKS))
        best_seller_links = self.driver.find_elements(*self.BEST_SELLER_LINKS)
        assert len(best_seller_links) == 5, f'Expected 5 elements but only found {len(best_seller_links)}'

    # def verify_best_seller_menu(self, locator):
    #     best_seller_menu = self.find_elements(*self.MENU_LINKS)
    #
    #     for i in range(len(best_seller_menu)):
    #         link_to_clik = self.find_elements(*self.MENU_LINKS)[i]
    #         link_text = link_to_clik.text
    #         link_to_clik.click()
    #         self.verify_partial_text(link_text, *self.HEADER)