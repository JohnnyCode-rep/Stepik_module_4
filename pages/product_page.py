from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def go_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.VIEW_BASKET_BUTTON)
        button.click()

    def should_be_product_name(self):
        product_name = self.is_element_present(*ProductPageLocators.PRODUCT_NAME)
        assert product_name.text != 0, "Product name is not presented"

    def should_be_product_price(self):
        product_price = self.is_element_present(*ProductPageLocators.PRODUCT_PRICE)
        assert product_price.text != 0, "Product price is not presented"

    def should_be_basket_price(self):
        basket_price = self.is_element_present(*ProductPageLocators.BASKET_PRICE)
        assert basket_price.text != 0, "Basket price is not presented"

    def should_be_correct_messages_after_adding_to_basket(self):
        self.should_be_correct_product_name()
        self.should_be_correct_product_price()

    def should_be_correct_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        messages = self.browser.find_element(*ProductPageLocators.MESSAGES_AFTER_ADDING_TO_BASKET)
        assert product_name.text in messages.text, "Product name is not correct"

    def should_be_correct_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        messages = self.browser.find_element(*ProductPageLocators.MESSAGES_AFTER_ADDING_TO_BASKET)
        assert product_price.text in messages.text, "Product price is not correct"