import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session", autouse=True)
def global_browser():
    # Настройки Selene
    browser.config.base_url = "https://goldapple.ru/"
    browser.config.timeout = 200.0
    browser.config.window_width = 1280
    browser.config.window_height = 1024

    # Основные настройки для блокировки всплывающих окон
    options = Options()
    options.add_argument("--disable-notifications")  # Отключает уведомления
    options.add_argument("--disable-popup-blocking")  # Блокирует всплывающие окна
    options.add_argument("--disable-infobars")  # Отключает инфобары
    options.add_experimental_option(
        "prefs", {
            "profile.default_content_setting_values.notifications": 2,  # Блокировка уведомлений
            "profile.default_content_setting_values.popups": 0,  # Блокировка popup
            "profile.default_content_setting_values.geolocation": 2,  # Блокировка геолокации
        }
    )

    # Настройки ChromeOptions
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    # Инициализация драйвера
    browser.config.driver = webdriver.Chrome(options=options)
    browser.config.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    # Открываем базовую страницу
    browser.open("/")

    yield  # Все тесты выполняются здесь

    # Закрытие браузера после всех тестов
    browser.quit()

