from selene import browser, have, be
import allure

class Contact:

    @allure.step('Открытие страницы c товаром')
    def open_store(self):
        browser.open('')
        return self

    @allure.step('Закрытие попапа')
    def close_popap(self):
        browser.element('//button[.//span[contains(text(), "Нет, другой")]]').click()
        browser.element('[data-transaction-name="ga-modal-close-button"]').click()
        return self

    @allure.step('Переход на страницу контактной информации')
    def search_contact_info(self):
        browser.with_(timeout=10).execute_script("window.scrollTo(0, document.body.scrollHeight)")
        browser.element('a[href="/contacts#key-contacts"]').click()
        return self

    @allure.step('Проверка контактов')
    def contact(self):
        assert browser.element('section[data-scroll-id="key-contacts"] a[href^="tel:"]').should(be.visible)
        assert browser.element('section[data-scroll-id="key-contacts"] a[href^="tel:"]').should(have.text("8 800 770 70 21"))

        assert (browser.element('//section[h2[contains(text(), "пресс-служба")]]'
                     '//a[@data-transaction-name="ga-info-contacts-email"]')
        .should(be.visible)
        .should(have.text('mediaoffice@goldapple.ru'))
        .should(have.attribute('href').value('mailto:mediaoffice@goldapple.ru')))

        assert (browser.element('//section[h2[contains(text(), "корпоративные заказы")]]'
                     '//a[@data-transaction-name="ga-info-contacts-email"]')
        .should(be.visible)
        .should(have.text('b2b@goldapple.ru'))
        .should(have.attribute('href').value('mailto:b2b@goldapple.ru')))

contact = Contact()