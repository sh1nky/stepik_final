from pages.product_page import ProductPage
import pytest


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param(
                                    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                    marks=pytest.mark.xfail(reason='some bug')),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
                                  ]
                         )
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_card()
    # page.should_be_item_price_on_page_equal_item_price_on_basket()
    page.should_be_item_name_on_page_equal_item_name_on_basket()
    # page.should_be_item_price_on_page_equal_item_price_on_basket_total()

@pytest.mark.xfail(reason='success message present')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0')
    page.open()
    page.add_item_to_card()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0')
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason='success message is not disappeared')
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0')
    page.open()
    page.add_item_to_card()
    page.should_be_success_message_is_disappeared()
