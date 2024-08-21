import time

import allure
import pytest

from data import ImportantQuestionData, Urls
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestQuestion:

    @allure.title('Проверка ответов на Важные вопросы')
    @allure.description('Кликаем на вопросы и проверяем текст ответов')
    @pytest.mark.parametrize(ImportantQuestionData.param, ImportantQuestionData.value)
    def test_important_question(self, driver, question, expected_answer):
        main_page = MainPage(driver)
        main_page.open_page(Urls.MAIN_PAGE)
        main_page.wait_and_find_element(MainPageLocators.COOKIES_BUTTON).click()
        question_heading = main_page.get_important_answer_heading(question)
        driver.execute_script("arguments[0].scrollIntoView(true);", question_heading)
        time.sleep(1)
        question_heading.click()
        answer = main_page.wait_and_find_element(MainPageLocators.ACCORDION_BUTTON_TEXT).text
        assert answer == expected_answer
