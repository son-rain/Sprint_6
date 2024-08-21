from selenium.webdriver.common.by import By


class BasePageLocators:
    YANDEX_LOGO = [By.XPATH, '//a[contains (@class, "Header_LogoYandex")]']
    SCOOTER_LOGO = [By.XPATH, '//a[contains (@class, "Header_LogoScooter")]']