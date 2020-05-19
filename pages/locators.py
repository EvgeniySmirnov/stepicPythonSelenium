from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") 

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    BOOK_ADDED_MESSAGE = (By.CSS_SELECTOR, "div.alert-success:nth-child(1) strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success")
    
    BOOK_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert-info strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    
