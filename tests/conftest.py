import pytest
import os
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv


# Загрузка переменных окружения
@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


# Добавление кастомной опции для pytest
def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='128.0',
        help='Версия браузера для тестов'
    )


# Фикстура с учетными данными
@pytest.fixture
def auth_credentials():
    return {
        'email': os.getenv('EMAIL'),
        'password': os.getenv('PASSWORD')
    }


# Основная фикстура для браузера
@pytest.fixture(scope="session", autouse=True)
def global_browser(request):
    # Получаем версию браузера из параметров
    browser_version = request.config.getoption('--browser_version')

    # Настройки Selene
    browser.config.base_url = "https://goldapple.ru/"
    browser.config.timeout = 10.0
    browser.config.window_width = 1280
    browser.config.window_height = 1024

    # Настройки ChromeOptions
    options = Options()

    # Общие настройки
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )

    # Экспериментальные опции
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option(
        "prefs", {
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_values.popups": 0,
            "profile.default_content_setting_values.geolocation": 2,
        }
    )

    # Настройки для Selenoid (если используются)
    if os.getenv("SELENOID_URL"):
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        options.capabilities.update(selenoid_capabilities)

        selenoid_login = os.getenv("SELENOID_LOGIN")
        selenoid_pass = os.getenv("SELENOID_PASS")
        selenoid_url = os.getenv("SELENOID_URL")

        driver = webdriver.Remote(
            command_executor=f"https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub",
            options=options
        )
    else:
        # Локальный запуск
        driver = webdriver.Chrome(options=options)

    # Настройка драйвера для Selene
    browser.config.driver = driver
    browser.config.driver.execute_script(
        "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
    )

    # Открываем базовую страницу
    browser.open("/")

    yield  # Все тесты выполняются здесь

    # Закрытие браузера после всех тестов
    browser.quit()