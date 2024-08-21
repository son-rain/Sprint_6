import allure
from selenium.webdriver import Keys

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step('Заполняем поле Имя')
    def set_name_input(self, name):
        name_input = self.wait_and_find_element(OrderPageLocators.NAME_FIELD)
        name_input.send_keys(name)

    @allure.step('Заполняем поле Фамилия')
    def set_surname_input(self, surname):
        surname_input = self.wait_and_find_element(OrderPageLocators.SURNAME_FIELD)
        surname_input.send_keys(surname)

    @allure.step('Заполняем поле Адрес')
    def set_address_input(self, address):
        address_input = self.wait_and_find_element(OrderPageLocators.ADDRESS_FIELD)
        address_input.send_keys(address)

    @allure.step('Заполняем поле Телефон')
    def set_phone_input(self, phone_number):
        phone_input = self.wait_and_find_element(OrderPageLocators.PHONE_NUMBER_FIELD)
        phone_input.send_keys(phone_number)

    @allure.step('Выбираем станцию метро')
    def choose_metro_station(self, station):
        self.wait_and_find_element(OrderPageLocators.METRO_STATION_SELECTOR).click()
        self.wait_and_find_element(OrderPageLocators.get_metro_station_button(station)).click()

    @allure.step('Нажимаем кнопку Далее')
    def click_next_button(self):
        button = self.wait_and_find_element(OrderPageLocators.NEXT_BUTTON)
        button.click()

    @allure.step('Выбираем дату')
    def choose_date(self, date):
        date_input = self.wait_and_find_element(OrderPageLocators.DATE_FIELD)
        date_input.send_keys(date)
        date_input.send_keys(Keys.RETURN)

    @allure.step('Выбираем период аренды')
    def choose_rental_period(self, period):
        self.wait_and_find_element(OrderPageLocators.RENTAL_PERIOD_FIELD).click()
        self.wait_and_find_element(OrderPageLocators.pick_rental_period(period)).click()

    @allure.step('Выбираем цвет самоката')
    def choose_color(self, color):
        self.wait_and_find_element(OrderPageLocators.pick_scooter_color(color)).click()

    @allure.step('Заполняем поле Комментарий для курьера')
    def set_comment_input(self, text):
        comment_input = self.wait_and_find_element(OrderPageLocators.COMMENT_FIELD)
        comment_input.send_keys(text)

    @allure.step('Нажимаем кнопку Заказать')
    def click_order_button(self):
        button = self.wait_and_find_element(OrderPageLocators.MAKE_ORDER_BUTTON)
        button.click()

    @allure.step('Нажимаем кнопку Да в модальном окне')
    def click_yes_button(self):
        button = self.wait_and_find_element(OrderPageLocators.ORDER_MODAL_BUTTON_YES)
        button.click()

    def make_order(self, name, surname, address, station, phone_number, date, period, color, comment):
        self.set_name_input(name)
        self.set_surname_input(surname)
        self.set_address_input(address)
        self.choose_metro_station(station)
        self.set_phone_input(phone_number)
        self.click_next_button()
        self.choose_date(date)
        self.choose_rental_period(period)
        self.choose_color(color)
        self.set_comment_input(comment)
        self.click_order_button()
        self.click_yes_button()
