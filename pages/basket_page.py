from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "URL is not correct"

    def check_basket_is_empty_text_is_present(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_TEXT), \
            "Basket-is-empty text is not presented"

    def check_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_NAME_IN_BASKET), \
            "The basket is not empty"
