import pytest
import os
from selene import browser
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
from pageobject.authorization_page import Authorization
from pathlib import Path
from utils import attach

# Явно указываем путь к .env в корне проекта
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_version",
        action="store",
        default="128",  # значение по умолчанию
        help="Specify browser version for tests"
    )


@pytest.fixture
def auth_credentials():
    return {
        'email': os.getenv('EMAIL'),
        'password': os.getenv('PASSWORD')
    }


@pytest.fixture
def authorization(auth_credentials):
    return Authorization(auth_credentials)


@pytest.fixture(scope="session", autouse=True)
def global_browser(request):
    # Проверка обязательных переменных окружения
    selenoid_login = os.getenv("SELENOID_LOGIN")
    selenoid_pass = os.getenv("SELENOID_PASS")
    selenoid_url = os.getenv("SELENOID_URL")

    if not all([selenoid_login, selenoid_pass, selenoid_url]):
        pytest.fail(
            "Selenoid credentials not configured. Set SELENOID_LOGIN, SELENOID_PASS and SELENOID_URL environment variables.")

    # Настройки Selene
    browser.config.base_url = "https://goldapple.ru/"
    browser.config.timeout = 10.0
    browser.config.window_width = 1280
    browser.config.window_height = 1024

    browser_version = request.config.getoption("--browser_version")
    options = Options()

    # Основные настройки для блокировки всплывающих окон
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
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    # Настройки Selenoid
    selenoid_capabilities = {
        "browserName": 'chrome',
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    # Инициализация драйвера для Selenoid
    driver = webdriver.Remote(
        command_executor=f'https://{selenoid_login}:{selenoid_pass}@{selenoid_url}/wd/hub',
        options=options
    )

    browser.config.driver = driver
    browser.config.window_height = 1280
    browser.config.window_width = 1024
    browser.config.base_url = "https://goldapple.ru/"

    # Скрываем WebDriver для обхода детекции
    browser.config.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    # Открываем базовую страницу
    browser.open("/")

    yield  # Все тесты выполняются здесь

    attach.add_screenshot(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    # Закрытие браузера после всех тестов
    browser.quit()