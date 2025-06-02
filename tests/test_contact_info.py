from selene import browser, have, be
import allure
from pageobject.contact_info import contact


@allure.story('Контактная информация')
def test_contact_info():
    contact.open_store().close_popap().search_contact_info().contact()
