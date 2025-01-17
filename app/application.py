from pages.main_page import MainPage
from pages.header import Header
from pages.cart_page import CartPage
from pages.search_result_page import SearchResultPage
from pages.best_seller_page import BestSellerPage
from pages.customer_service_page import CustomerServicePage
from pages.sign_in_page import SignInPage
from pages.product_page import ProductPage
from pages.amazon_not_found_page import NotFoundPage
from pages.amazon_blog import Blog
from pages.amazon_terms_conditions_page import AmazonTermsConditions


class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultPage(driver)
        self.cart_page = CartPage(driver)
        self.best_seller_page = BestSellerPage(driver)
        self.customer_service_page = CustomerServicePage(driver)
        self.sign_in_page = SignInPage(driver)
        self.product_page = ProductPage(driver)
        self.amazon_blog = Blog(driver)
        self.amazon_not_found_page = NotFoundPage(driver)
        self.amazon_terms_conditions_page = AmazonTermsConditions(driver)


# app = Application()
# app.main_page.open_main()
# app.header.search_product()
