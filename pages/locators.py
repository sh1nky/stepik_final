from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    #  login form
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    LOGIN_BUTTON_SUBMIT = (By.CSS_SELECTOR, 'button[name="login_submit"]')
    LOGIN_INPUT_EMAIL = (By.CSS_SELECTOR, 'input #id_login-username')
    LOGIN_INPUT_PASSWORD = (By.CSS_SELECTOR, 'input #id_login-password')

    #  register form
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTER_BUTTON_SUBMIT = (By.CSS_SELECTOR, 'button[name="registration_submit"]')
    REGISTER_INPUT_EMAIL = (By.CSS_SELECTOR, 'input #id_registration-email')
    REGISTER_INPUT_PASSWORD = (By.CSS_SELECTOR, 'input #id_registration-password')
    REGISTER_INPUT_REPEAT_PASSWORD = (By.CSS_SELECTOR, 'input #id_registration-password2')

