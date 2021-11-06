# from chromedriver_py import binary_path
# browser = webdriver.Chrome(executable_path=binary_path)
from selenium import webdriver
from chromedriver_py import binary_path # this will get you the path variable
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome(executable_path=binary_path)
    browser.get(link)

    # Находим обязательные поля
    first_name = browser.find_element_by_xpath("//input[contains (@class, 'first') and @required]")
    second_name = browser.find_element_by_xpath("//input[contains (@class, 'second') and @required]")
    email = browser.find_element_by_xpath("//input[contains (@class, 'third') and @required]")

    # Помещаем обязательные поля в список
    required_elements = [first_name, second_name, email]

    # Заполняем обязательные поля
    for element in required_elements:
        element.send_keys("ssseeerrr")

    #смотрим на заполненные поля
    time.sleep(5)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
