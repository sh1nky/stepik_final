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


class ProductPageLocators:
    BUTTON_ADD_TO_CARD = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    ITEM_NAME_ON_PAGE = (By.CSS_SELECTOR, "div.product_main h1")
    ITEM_PRICE_ON_PAGE = (By.CSS_SELECTOR, "div.product_main p.price_color")

    ITEM_NAME_ON_BASKET = (By.CSS_SELECTOR, "div.alert-success div.alertinner strong")
    ITEM_PRICE_ON_BASKET = (By.CSS_SELECTOR, "div.alert-info div.alertinner strong")

    PRICE_BASKET_TOTAL = (By.CSS_SELECTOR, "div.basket-mini")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success div.alertinner")
