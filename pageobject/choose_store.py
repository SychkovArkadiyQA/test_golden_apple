from selene import browser, have, by
import allure

class Store:

    @allure.step('Открытие страницы')
    def choose_store(self):
        browser.open('')
        return self

    @allure.step('Закрытие попапа')
    def close_popap(self):
        browser.element('//button[.//span[contains(text(), "Нет, другой")]]').click()
        return self

    @allure.step('Выбор адреса доставки')
    def choose_address(self):
        browser.element('div[name="streetHouse"] input').type("Мира 1")
        browser.element('//div[contains(@class, "option-content")]//span[contains(text(), "ул Мира, д 1")]').click()
        browser.element(by.text('привезти сюда')).click()
        return self

    @allure.step('Проверка успешно установленного адреса')
    def assert_successful_choose_address(self):
        assert browser.driver.current_url == 'https://goldapple.ru/'
        assert browser.element('div.yrOdr.AN1pf').should(have.text('Мира'))
        assert browser.element('div.yrOdr.AN1pf').should(have.text('1'))

store = Store()


