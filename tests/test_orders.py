import time

import allure

from data import Urls
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from locators.order_page_locators import OrderPageLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrders:
    @allure.title('Проверка оформления заказа через кнопку в шапке сайта')
    def test_header_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)

        main_page.wait_and_find_element(MainPageLocators.HEADER_ORDER_BUTTON).click()

        order_page = OrderPage(driver)
        order_page.make_order("Никита", "Каверин", "Лубянка, 8", "Сокольники",
                              "89087689090", "14.09.2024", "сутки", "чёрный жемчуг", "Во дворе лужа")
        assert main_page.wait_text_and_find_element(OrderPageLocators.ORDER_SUCCESS_MODAL,
                                                    "Заказ оформлен").is_displayed()
        order_page.wait_and_find_element(OrderPageLocators.GET_STATUS_ORDER_BUTTON).click()
        order_page.wait_and_find_element(BasePageLocators.SCOOTER_LOGO).click()
        assert driver.current_url == Urls.MAIN_PAGE
        main_page.wait_and_find_element(BasePageLocators.YANDEX_LOGO).click()
        main_page.wait_dzen_page()
        assert driver.current_url == Urls.DZEN_PAGE

    @allure.title('Проверка оформления заказа через кнопку внизу страницы')
    def test_middle_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)

        order_button = main_page.wait_and_find_element(MainPageLocators.HOME_FINISH_ORDER_BUTTON)
        driver.execute_script("arguments[0].scrollIntoView(true);", order_button)
        time.sleep(1)
        order_button.click()

        order_page = OrderPage(driver)
        order_page.make_order("Олеся", "Крутова", "Маросейко, 8", "Черкизовская",
                              "89680965643", "01.09.2024", "двое суток", "серая безысходность", "")
        assert main_page.wait_text_and_find_element(OrderPageLocators.ORDER_SUCCESS_MODAL,
                                                    "Заказ оформлен").is_displayed()
        order_page.wait_and_find_element(OrderPageLocators.GET_STATUS_ORDER_BUTTON).click()
        order_page.wait_and_find_element(BasePageLocators.SCOOTER_LOGO).click()
        assert driver.current_url == Urls.MAIN_PAGE
        main_page.wait_and_find_element(BasePageLocators.YANDEX_LOGO).click()
        main_page.wait_dzen_page()
        assert driver.current_url == Urls.DZEN_PAGE
