import allure
from selene import browser, have
from pageobject.authorization_page import authorization

@allure.story('Успешная авторизация')
def test_successful_authorization():
    authorization.open_authorization_page().choose_address().open_authorization_sidebar(
    ).authorization_ya().choose_address_2().assert_successful_authorization()

