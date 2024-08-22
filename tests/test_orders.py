import allure

from data import Urls
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrders:
    @allure.title('Проверка оформления заказа через кнопку в шапке сайта')
    def test_header_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)

        main_page.click_nav_order_button()

        order_page = OrderPage(driver)
        order_page.make_order("Никита", "Каверин", "Лубянка, 8", "Сокольники",
                              "89087689090", "14.09.2024", "сутки", "чёрный жемчуг", "Во дворе лужа")
        assert order_page.wait_modal_window_is_displayed()

        order_page.click_status_order()
        order_page.click_scooter_logo()
        assert driver.current_url == Urls.MAIN_PAGE

        main_page.click_yandex_logo()
        main_page.wait_dzen_page()
        assert driver.current_url == Urls.DZEN_PAGE

    @allure.title('Проверка оформления заказа через кнопку внизу страницы')
    def test_middle_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)

        main_page.click_middle_order_button()

        order_page = OrderPage(driver)
        order_page.make_order("Олеся", "Крутова", "Маросейко, 8", "Черкизовская",
                              "89680965643", "01.09.2024", "двое суток", "серая безысходность", "")
        assert order_page.wait_modal_window_is_displayed()

        order_page.click_status_order()
        order_page.click_scooter_logo()
        assert driver.current_url == Urls.MAIN_PAGE

        main_page.click_yandex_logo()
        main_page.wait_dzen_page()
        assert driver.current_url == Urls.DZEN_PAGE
