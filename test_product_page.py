from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_message_book_added()
    page.should_be_basket_price_eq_book_price()

    
    