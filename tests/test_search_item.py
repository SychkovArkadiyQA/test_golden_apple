import allure
from pageobject.search_item import search

@allure.story('Выбор магазина для самовывоза')
def test_successful_choose_address():
    search.open_store().close_popap().search_tap().search_item().verify_search_results()







