from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "span > a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "[name='registration-email']")
    REGISTER_PASSWORD_1 = (By.CSS_SELECTOR, "[name='registration-password1']")
    REGISTER_PASSWORD_2 = (By.CSS_SELECTOR, "[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "div.alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")


class BasketPageLocators():
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "h3 > a")
