from selene.support import webdriver
from pageobject.authorization_page import Authorization
import allure
from selene import browser, have

@allure.story('Успешная авторизация')
def test_successful_authorization():
    pass

@allure.story('Открытие страницы')
def test_open_authorization_page():
    browser.open('')

@allure.story('Пропуск выбора адреса')
def test_choose_address():
    browser.element('//button[.//span[contains(text(), "Нет, другой")]]').click()
    browser.element('[data-transaction-name="ga-modal-close-button"]').click()

@allure.story('Открытие сайдбара авторизации')
def test_open_authorization_sidebar():
    browser.element('//*[contains(@class, "ga-visually-hidden") and text()="Авторизация"]/..').click()

@allure.story('Авторизация через Яндекс ID')
def test_authorization_ya():
    browser.element('[data-transaction-name="ga-auth-modal-auth-services"]').click()
    browser.element('button.LoginWithPhonePage-button').click()
    browser.element('[data-t="field:input-login"]').type('email')
    browser.element('#passp\\:sign-in').click()
    browser.element('#passp-field-passwd').type('pass')
    browser.element('#passp\\:sign-in').click()

@allure.story('Авторизация через Яндекс ID')
def test_authorizati_ya():
    browser.element('[data-transaction-name="ga-auth-modal-auth-services"]').click()