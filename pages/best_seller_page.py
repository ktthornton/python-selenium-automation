from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BestSellerPage(Page):
    BEST_SELLER_LINKS = (By.CSS_SELECTOR, '#zg_header a')

    def verify_best_seller_links(self):
        wait = WebDriverWait(self.driver, 10)
        self.driver.wait.until(EC.visibility_of_all_elements_located(self.BEST_SELLER_LINKS))
        best_seller_links = self.driver.find_elements(*self.BEST_SELLER_LINKS)
        assert len(best_seller_links) == 5, f'Expected 5 elements but only found {len(best_seller_links)}'

