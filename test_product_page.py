from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
import time
import pytest

PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

#def test_guest_can_add_product_to_basket(browser):
def tst_guest_can_add_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.should_not_be_success_message()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_message_book_added()
    page.should_be_basket_price_eq_book_price()
    

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.should_not_be_success_message()
    

def test_message_disappeared_after_adding_product_to_basket(browser): 
    page = ProductPage(browser, PRODUCT_LINK)
    page.open()
    page.add_product_to_basket()
    page.should_disappeared_success_message()

    