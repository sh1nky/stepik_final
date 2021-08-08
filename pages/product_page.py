from .base_page import BasePage
from .locators import ProductPageLocators
import re

class ProductPage(BasePage):

    def add_item_to_card(self):
        self.click_add_to_card_button()
        self.solve_quiz_and_get_code()

    def click_add_to_card_button(self):
        assert self.is_element_present(*ProductPageLocators.BUTTON_ADD_TO_CARD), 'Button "Add to card" is not presented'
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CARD).click()

    def should_be_item_price_on_page(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_PRICE_ON_PAGE), \
            "Price item on page is not presented"

    def should_be_item_price_on_basket(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_PRICE_ON_BASKET), \
            "Price item on page is not presented"

    def should_be_total_price_on_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_BASKET_TOTAL), \
            "Total basket price is not presented"

    def should_be_item_name_on_page(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_NAME_ON_PAGE), \
            "Item name on page is not presented"

    def should_be_item_name_on_basket(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_NAME_ON_BASKET), \
            "Item name on basket is not presented"

    def should_be_item_price_on_page_equal_item_price_on_basket(self):

        page_price = self.get_item_price_on_page()
        basket_price = self.get_item_price_on_basket()

        assert page_price == basket_price, \
            f"Price item on page not equal price on basket ([{page_price}] != [{basket_price}])"

    def should_be_item_name_on_page_equal_item_name_on_basket(self):
        page_name = self.get_item_name_on_page()
        basket_name = self.get_item_name_on_basket()

        assert page_name == basket_name, \
            f"Item name on page not equal item name on basket ([{page_name}] != [{basket_name}])"

    def should_be_item_price_on_page_equal_item_price_on_basket_total(self):
        page_price = self.get_item_price_on_page()
        total_basket_price = self.get_total_basket_price()

        assert page_price == total_basket_price, \
            f"Item price on page not equal price on total basket ([{page_price}] != [{total_basket_price}])"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented"

    def should_be_success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"

    def get_item_price_on_page(self):
        self.should_be_item_price_on_page()

        return self.browser.find_element(*ProductPageLocators.ITEM_PRICE_ON_PAGE).text.strip()

    def get_item_price_on_basket(self):
        self.should_be_item_price_on_basket()

        return self.browser.find_element(*ProductPageLocators.ITEM_PRICE_ON_BASKET).text.strip()

    def get_total_basket_price(self):
        self.should_be_total_price_on_basket()

        price = self.browser.find_element(*ProductPageLocators.PRICE_BASKET_TOTAL).text.strip()
        price = re.search(r'(\s.?\d+\.\d+\s?.?\s)', price)

        return price.group(0).strip()

    def get_item_name_on_page(self):
        self.should_be_item_name_on_page()

        return self.browser.find_element(*ProductPageLocators.ITEM_NAME_ON_PAGE).text.strip()

    def get_item_name_on_basket(self):
        self.should_be_item_name_on_basket()

        return self.browser.find_element(*ProductPageLocators.ITEM_NAME_ON_BASKET).text.strip()
