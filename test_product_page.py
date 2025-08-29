from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    # link = "https://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(5)
    page.check_product_name()
    page.check_product_price()
