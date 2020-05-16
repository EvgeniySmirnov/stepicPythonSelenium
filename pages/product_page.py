from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()

    def should_be_message_book_added(self):
        book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        message_text = self.browser.find_element(*ProductPageLocators.BOOK_ADDED_MESSAGE).text
        assert book_name == message_text, f"Book name {book_name} not equals name in message {message_text}"

    def should_be_basket_price_eq_book_price(self):
        book_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        assert book_price == basket_price, f"Book price {book_price} not equals price in message {basket_price}"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
        "Success message is presented, but should not be"