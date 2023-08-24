from pages.base_page import Page
from selenium.webdriver.common.by import By


class CustomerServicePage(Page):
    CS_HEADER = (By.CSS_SELECTOR, 'h1[class="fs-heading bolded"]')
    CS_SEARCH_BAR = (By.ID, 'hubHelpSearchInput')
    CS_TEXT_HEADER = (By.CSS_SELECTOR, 'h2[class="fs-heading bolded"]')  # 'Search our help library' and 'All help topics' headers
    CS_DIRECTORY_LINKS = (By.CSS_SELECTOR, '.fs-match-card-title.full')
    CS_TOPICS_COLUMN = (By.CSS_SELECTOR, '[for*="foresight-help-topic"]')

    def verify_cs_elements(self):
        self.find_element(*self.CS_HEADER)
        self.find_element(*self.CS_SEARCH_BAR)

        cs_text_header = self.driver.find_elements(*self.CS_TEXT_HEADER)
        assert len(cs_text_header) == 2, f'Expected 2 elements but only found {len(cs_text_header)}'

        cs_directory_links = self.driver.find_elements(*self.CS_DIRECTORY_LINKS)
        assert len(cs_directory_links) == 11, f'Expected 11 elements but only found {len(cs_directory_links)}'

        cs_topic_links = self.driver.find_elements(*self.CS_TOPICS_COLUMN)
        assert len(cs_topic_links) == 11, f'Expected 11 elements but only found {len(cs_topic_links)}'