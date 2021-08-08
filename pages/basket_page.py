from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_basket_form(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORM), \
            "Basket form is presented"

    def should_be_basket_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), \
            "Basket epmty text not presented"

    def validate_empty_basket_text(self):
        self.should_be_basket_empty_text()
        text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text

        assert 'Your basket is empty.' in text, f'Text "Your basket is empty." not found in {text}'