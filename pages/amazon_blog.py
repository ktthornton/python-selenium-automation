from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.common.by import By


class Blog(Page):

    def verify_opened(self):
        self.verify_partial_url('www.aboutamazon.com')