import allure
from pageobject.choose_store import store


@allure.story('Выбор магазина для самовывоза')
def test_successful_choose_address():
    store.choose_store().close_popap().choose_address().assert_successful_choose_address()






