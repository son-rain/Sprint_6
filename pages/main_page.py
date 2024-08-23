import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Находим элемент страницы с вопросом и кликаем по нему")
    def get_important_answer_heading_and_click(self, question):
        locator = MainPageLocators.get_question_heading(question)
        question_heading = self.wait_and_find_element(locator)
        self.scroll_to_element(question_heading)
        self.wait_element(locator)
        question_heading.click()

    @allure.step("Получаем текст ответа на вопрос")
    def get_accordion_answer_text(self):
        return self.wait_and_find_element(MainPageLocators.ACCORDION_BUTTON_TEXT).text

    @allure.step("Кликаем на логотип Яндекса")
    def click_yandex_logo(self):
        self.wait_and_find_element(BasePageLocators.YANDEX_LOGO).click()

    @allure.step("Кликаем на кнопку заказа в середине страницы")
    def click_middle_order_button(self):
        locator = MainPageLocators.HOME_FINISH_ORDER_BUTTON
        order_button = self.wait_and_find_element(locator)
        self.scroll_to_element(order_button)
        self.wait_element(locator)
        order_button.click()



