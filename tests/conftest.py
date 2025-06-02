import pytest
import os
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


def pytest_addoption(parser):
    parser.addoption(
        "--browser_version",
        action="store",
        default="128",
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


@pytest.fixture(scope="function")  # Изменено с session на function
def setup_browser(request):
    browser_version = request.config.getoption("--browser_version")

    # Общие настройки для браузера
    options = Options()

    # Блокировка всплывающих окон и уведомлений
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-infobars")
    options.add_experimental_option(
        "prefs", {
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_setting_values.popups": 0,
            "profile.default_content_setting_values.geolocation": 2,
        }
    )

    # Настройки для обхода детекции автоматизации
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )

    # Инициализация браузера
    browser.config.driver_options = options
    browser.config.base_url = "https://goldapple.ru/"
    browser.config.timeout = 10.0
    browser.config.window_width = 1280
    browser.config.window_height = 1024

    # Открытие базовой страницы
    browser.open("/")

    yield browser

    # Очистка куков и закрытие браузера после каждого теста
    browser.clear_cookies()
    browser.quit()


@pytest.fixture
def app(setup_browser):
    yield setup_browser
