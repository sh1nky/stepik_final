from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'String "login" not in current url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.fill_input_register_email(email)
        self.fill_input_register_password(password)
        self.fill_input_register_repeat_password(password)

        self.click_register_button_submit()

    def should_be_register_input_email(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_INPUT_EMAIL), \
            "Register input email is not presented"

    def should_be_register_input_password(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_INPUT_PASSWORD), \
            "Register input password is not presented"

    def should_be_register_input_repeat_password(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_INPUT_REPEAT_PASSWORD), \
            "Register input repeat password is not presented"

    def should_be_register_button_submit(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON_SUBMIT), \
            "Register button submit is not presented"

    def fill_input_register_email(self, email):
        self.should_be_register_input_email()
        self.browser.find_element(*LoginPageLocators.REGISTER_INPUT_EMAIL).send_keys(email)

    def fill_input_register_password(self, email):
        self.should_be_register_input_password()
        self.browser.find_element(*LoginPageLocators.REGISTER_INPUT_PASSWORD).send_keys(email)

    def fill_input_register_repeat_password(self, email):
        self.should_be_register_input_repeat_password()
        self.browser.find_element(*LoginPageLocators.REGISTER_INPUT_REPEAT_PASSWORD).send_keys(email)

    def click_register_button_submit(self):
        self.should_be_register_button_submit()
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON_SUBMIT).click()
