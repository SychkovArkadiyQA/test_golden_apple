from selene import browser, have
import allure

class Search:

    @allure.step('Открытие страницы')
    def open_store(self):
        browser.open('')
        return self

    @allure.step('Закрытие попапа')
    def close_popap(self):
        browser.element('//button[.//span[contains(text(), "Нет, другой")]]').click()
        browser.element('[data-transaction-name="ga-modal-close-button"]').click()
        return self

    @allure.step('Тап по поиску')
    def search_tap(self):
        browser.element('button.ga-header__tab_type_search').click()
        return self

    @allure.step('Ввод названия товара')
    def search_item(self):
        browser.element('//input[@placeholder="хочу купить" and @enterkeyhint="search"]').type("bobber термос").press_enter()
        return self

    @allure.step('Проверка результатов поиска')
    def verify_search_results(self):
        assert browser.element('//div[contains(@class, "nhaFs")][normalize-space()="термос"]')
        assert browser.element('//span[contains(@class, "_57-lB") and contains(text(), "Bobber")]')

search = Search()