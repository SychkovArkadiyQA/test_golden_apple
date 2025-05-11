from selene import browser, have
import allure


class Authorization:

    @allure.step('Открытие страницы')
    def open_authorization_page(self):
        browser.open('')
        return self

    @allure.step('Пропуск выбора адреса')
    def choose_address(self):
        browser.element('//button[.//span[contains(text(), "Нет, другой")]]').click()
        browser.element('[data-transaction-name="ga-modal-close-button"]').click()
        return self

    @allure.step('Открытие сайдбара авторизации')
    def open_authorization_sidebar(self):
        browser.element('//*[contains(@class, "ga-visually-hidden") and text()="Авторизация"]/..').click()
        return self

    @allure.step('Авторизация через Яндекс ID')
    def authorization_ya(self):
        browser.element('[data-transaction-name="ga-auth-modal-auth-services"]').click()
        browser.element('button.LoginWithPhonePage-button').click()
        browser.element('[data-t="field:input-login"]').type('email')
        browser.element('#passp\\:sign-in').click()
        browser.element('#passp-field-passwd').type('pass')
        browser.element('#passp\\:sign-in').click()
        browser.element('//button[.//span[text()="Войти как SummerSTR"]]').click()
        return self

    @allure.step('Пропуск выбора адреса #2')
    def choose_address_2(self):
        browser.element('//button[.//span[contains(text(), "Нет, другой")]]').click()
        browser.element('[data-transaction-name="ga-modal-close-button"]').click()
        return self

    @allure.step('Проверка успешной авторизации')
    def assert_successful_authorization(self):
        assert browser.driver.current_url == 'https://goldapple.ru/customer/account/orders'

authorization = Authorization()