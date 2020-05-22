from .base_page import BasePage
from .locators import LoginPageLocators

import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        curr_url = self.browser.current_url
        assert "login" in curr_url, f"'login' not in current url: '{curr_url}''"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email) 
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_PASSWORD1).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()
