from selene import browser, have
import allure


class Authorization:

    @allure.step('Открытие страницы')
    def open_authorization_page(self):
        browser.open('')
        return self

    @allure.step('Открытие сайдбара авторизации')
    def open_authorization_page(self):
        browser.element('#ga-visually-hidden').click()
        return self