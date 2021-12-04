import time


class TestCheckCatalogue():

    def test_check_basket_button(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        browser.get(link)
        time.sleep(30)
        basket_button = browser.find_element_by_css_selector('.btn-add-to-basket')
        browser.execute_script("return arguments[0].scrollIntoView(true);", basket_button)
        assert basket_button, 'Кнопка не найдена'
        #btn btn-lg btn-primary btn-add-to-basket
