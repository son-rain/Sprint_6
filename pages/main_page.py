import time

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def get_important_answer_heading(self, question):
        accordion_heading = MainPageLocators.get_question_heading(question)
        return self.wait_text_and_find_element(accordion_heading, question)



