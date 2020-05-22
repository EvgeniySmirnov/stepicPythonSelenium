from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_message_bascet_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASCET_IS_EMPTY), \
        "Сообщение 'Ваша корзина пустая' не найдено на странице"

    def should_not_be_bascet_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASCET_ITEMS), \
        "Корзина содержит товары, а не должна"