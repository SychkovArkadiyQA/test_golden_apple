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

@allure.story('Открытие сайдбара авторизации')
def test_open_authorization_sidebar():
    browser.element('//*[contains(@class, "ga-visually-hidden") and text()="Авторизация"]/..').click()

@allure.story('Авторизация через Яндекс ID')
def test_authorization_ya():
    browser.element('//button[contains(@class, "Gt8pH")]//i[contains(@class, "yUKnh")]').click()