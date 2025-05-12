import allure
from pageobject.cart_page import cart

@allure.story('Добавление товара в корзину')
def test_successful_add_to_cart():
    cart.open_store().close_popap().add_to_cart().move_to_cart().check_cart()

@allure.story('Добавление нескольких товаров в корзину')
def test_successful_add_2_to_cart():
    cart.open_store().close_popap().add_2_to_cart().move_to_cart().check_cart_2()
