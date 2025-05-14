from selene import browser, have, be
import allure
from pageobject.contact_info import contact


#В тесте есть явная ошибка. Не получается проскролить страницу до конца. Приходится "помогать" вручную
@allure.story('Контактная информация')
def test_contact_info():
    contact.open_store().close_popap().search_contact_info().contact()
