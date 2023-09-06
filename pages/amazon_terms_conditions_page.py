from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class AmazonTermsConditions(Page):
    PRIVACY_NOTICE = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")

    def open_terms_conditions(self):
        self.driver.get('https://www.amazon.com/gp/help/customer/display.html/'
                        'ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')

    def click_privacy_notice(self, *locator):
        self.driver.find_element(*self.PRIVACY_NOTICE).click()


