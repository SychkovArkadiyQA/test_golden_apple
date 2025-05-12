from selene import browser, have
import allure
import time

class Cart:

    @allure.step('Открытие страницы c товаром')
    def open_store(self):
        browser.open('19000233577-cayenne-red')
        return self

    @allure.step('Закрытие попапа')
    def close_popap(self):
        browser.element('//button[.//span[contains(text(), "Нет, другой")]]').click()
        browser.element('[data-transaction-name="ga-modal-close-button"]').click()
        return self

    @allure.step('Добавление товара в корзину')
    def add_to_cart(self):
        browser.element('button._15pyi.h5YKb').click()
        return self

    @allure.step('Добавление двух товаров в корзину')
    def add_2_to_cart(self):
        browser.element('button._15pyi.h5YKb').click()
        time.sleep(2)
        browser.element('button._15pyi.h5YKb').click()
        return self

    @allure.step('Переход к корзину')
    def move_to_cart(self):
        browser.element('button.ga-header__tab_type_cart').click()
        return self

    @allure.step('Проверка что в корзине появился нужный товар в нужно количестве')
    def check_cart(self):
        assert browser.element('[data-transaction-name="ga-cart-item-heading"]').should(
            have.text('BOBBER cayenne red'))
        assert browser.element('span._9M-Nj').should(have.text('1 шт.'))
        return self

    @allure.step('Проверка что в корзине несколько товаров')
    def check_cart_2(self):
        assert browser.element('[data-transaction-name="ga-cart-item-heading"]').should(
            have.text('BOBBER cayenne red'))
        assert browser.element('span._9M-Nj').should(have.text('2 шт.'))
        return self

cart = Cart()

