from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select


class SearchResultPage(Page):
    SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
    PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2 span.a-text-normal')
    PRODUCT_IMG = (By.CSS_SELECTOR, '.s-image[data-image-latency="s-product-image"]')
    SUBHEADER_DEPT = (By.CSS_SELECTOR, 'data-category=["{SUB_STR}"]')

    def _get_subheader_dept_locator(self, dept):
        # return SUBHEADER_DEPT with {SUB_STR} replaced

        # return [By.CSS_SELECTOR, 'data-category=["dept"]']
        return [self.SUBHEADER_DEPT[0], self.SUBHEADER_DEPT[1].replace('{SUB_STR}', dept)]

    def verify_search_result(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def click_first_product(self):
        self.driver.find_element(*self.PRODUCT_PRICE).click()
        sleep(2)

    def verify_results_name_img(self):
        all_products = self.driver.find_elements(*self.SEARCH_RESULTS)

        for product in all_products:
            product_title = product.find_element(*self.PRODUCT_TITLE).text
            print(product_title)
            assert product_title, 'Product title not shown'
            product.find_element(*self.PRODUCT_IMG)

    # def verify_dept_selected(self, dept):
    #     subheader_locator = self._get_subheader_dept_locator(dept)
    #     self.find_element(*subheader_locator)
