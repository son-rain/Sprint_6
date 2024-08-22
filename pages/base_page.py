import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators.base_page_locators import BasePageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Находим элемент на странице")
    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Находим элемент на странице по локатору и тексту")
    def wait_text_and_find_element(self, locator, text) -> WebElement:
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(locator, text))
        return self.driver.find_element(*locator)

    @allure.step("Ожидаем перехода на страницу Дзен")
    def wait_dzen_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains('https://dzen.ru/'))

    @allure.step("Кликаем на кнопку заказа вверху страницы")
    def click_nav_order_button(self):
        self.wait_and_find_element(BasePageLocators.HEADER_ORDER_BUTTON).click()

    @allure.step("Кликаем на логотип Самоката")
    def click_scooter_logo(self):
        self.wait_and_find_element(BasePageLocators.SCOOTER_LOGO).click()

    @allure.step("Открываем страницу")
    def open_page(self, url):
        self.driver.get(url)