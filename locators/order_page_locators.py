from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_FIELD = [By.XPATH, "//input[contains(@placeholder,'Имя')]"]
    SURNAME_FIELD = [By.XPATH, "//input[contains(@placeholder,'Фамилия')]"]
    ADDRESS_FIELD = [By.XPATH, "//input[contains(@placeholder,'Адрес')]"]
    PHONE_NUMBER_FIELD = [By.XPATH, "//input[contains(@placeholder,'Телефон')]"]
    METRO_STATION_SELECTOR = [By.CLASS_NAME, "select-search"]
    NEXT_BUTTON = [By.XPATH, "//button[text()='Далее']"]
    DATE_FIELD = [By.XPATH, "//input[contains(@placeholder,'Когда привезти самокат')]"]
    RENTAL_PERIOD_FIELD = [By.XPATH, '//div[contains(@class,"Dropdown-root")]']
    RENTAL_PERIOD_PICKER = [By.CLASS_NAME, 'Dropdown-option']
    COLOR_PICKER = [By.XPATH, "//input[@type='checkbox']/parent::label[contains(@class, 'Checkbox_Label')]"]
    COMMENT_FIELD = [By.XPATH, "//input[contains(@placeholder,'Комментарий для курьера')]"]
    MAKE_ORDER_BUTTON = [By.XPATH, "//div[contains (@class,'Order_Buttons')]/button[text()='Заказать']"]
    ORDER_MODAL_BUTTON_YES = [By.XPATH, "//div[contains (@class,'Order_Modal')]//button[text()='Да']"]
    ORDER_SUCCESS_MODAL = [By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]"]
    GET_STATUS_ORDER_BUTTON = [By.XPATH, "//button[text()='Посмотреть статус']"]

    @staticmethod
    def get_metro_station_button(name):
        return By.XPATH, f"//div[contains (@class,'Order_Text') and text()='{name}']/parent::button"

    @staticmethod
    def pick_scooter_color(color):
        if color == 'серая безысходность':
            return By.ID, 'grey'
        elif color == 'чёрный жемчуг':
            return By.ID, 'black'

    @staticmethod
    def pick_rental_period(period):
        return By.XPATH, f'//div[contains(@class,"Dropdown-option") and text()="{period}"]'








