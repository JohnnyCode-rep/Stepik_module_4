from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET_BUTTON = (By.PARTIAL_LINK_TEXT, "basket")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, "[class='col-sm-6 product_main']>[class='price_color']")
    PRODUCT_NAME = (By.TAG_NAME, "h1")
    BASKET_PRICE = (By.CSS_SELECTOR, '[class="basket-mini pull-right hidden-xs"]')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    PRODUCT_NAME_IN_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRICE_IN_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')


class BasketPageLocators:
    PRODUCTS_IN_BASKET = (By.CLASS_NAME, "basket-title hidden-xs")
    MESSAGE_ABOUT_EMPTY_BASKET = [By.XPATH, '//*[@id="content_inner"]/p']
