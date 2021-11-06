# from chromedriver_py import binary_path
# browser = webdriver.Chrome(executable_path=binary_path)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from chromedriver_py import binary_path  # this will get you the path variable
import math
import time

try:
    # Открыть страницу
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome(executable_path=binary_path)
    browser.get(link)

    # Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
    price_field = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    if price_field:
        # Нажать на кнопку "Book"
        book_button = browser.find_element_by_id("book")
        book_button.click()

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    input_value = browser.find_element_by_id("input_value")
    input_value_text = int(input_value.text)


    def calc(x):
        return str(math.log(abs(12 * math.sin(x))))


    answer = calc(input_value_text)
    answer_field = browser.find_element_by_id("answer")
    answer_field.send_keys(answer)
    submit_button = browser.find_element_by_id("solve")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
