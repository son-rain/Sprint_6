from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_text_and_find_element(self, locator, text) -> WebElement:
        WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(locator, text))
        return self.driver.find_element(*locator)

    def wait_to_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))

    def wait_dzen_page(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.number_of_windows_to_be(2))
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains('https://dzen.ru/'))

    def open_page(self, url):
        self.driver.get(url)