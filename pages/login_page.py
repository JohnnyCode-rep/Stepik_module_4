from pages.base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "URL is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        Email = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        Email.send_keys(email)
        Password_1 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_1)
        Password_1.send_keys(password)
        Password_2 = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_2)
        Password_2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button.click()
        #time.sleep(100)
        assert self.is_element_present(*LoginPageLocators.ALERT_SUCCESS_REGISTRATION), "Registration failed"

