from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCORDION_BUTTON_TEXT = [By.XPATH, '//div[contains(@class, "accordion__panel") and not(@hidden)]/p']
    COOKIES_BUTTON = [By.ID, 'rcc-confirm-button']
    HEADER_ORDER_BUTTON = [By.XPATH, '//div[contains (@class, "Header_Nav")]/button[text()="Заказать"]']
    HOME_FINISH_ORDER_BUTTON = [By.XPATH, '//div[contains (@class, "Home_FinishButton")]/button[text()="Заказать"]']

    @staticmethod
    def get_question_heading(question):
        return By.XPATH, f'//div[contains(@class,"accordion__heading")]/child::div[text() = "{question}"]'

