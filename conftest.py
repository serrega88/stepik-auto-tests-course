import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

# Задаём браузер по умолчанию
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru, en, es, fr or other")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption('language')
    browser = None
    # Опции для выбора языка на основании данных браузера для Хрома
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    # Опции для выбора языка на основании данных браузера для Файрфокса
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)
    # Возможность выбирать браузер для запуска
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        browser.implicitly_wait(5)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=fp)
        browser.implicitly_wait(5)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()
