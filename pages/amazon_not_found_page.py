from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from selenium.webdriver.common.by import By


class NotFoundPage(Page):
    DOG_IMG = (By.ID, 'd')

    def store_original_window(self):
        return self.get_current_window()

    def click_dog_img(self):
        self.click(*self.DOG_IMG)