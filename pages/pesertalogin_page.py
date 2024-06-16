from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from utils.shopeeconfig_manager import ConfigManager

class LoginPage(BasePage):
    EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@placeholder="Password"]')
    LOGIN_BUTTON = (By.XPATH, '//a[normalize-space()="Login"]')
    BUTTON_MASUK = (By.XPATH, '//button[normalize-space()="Masuk"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.config = ConfigManager.get_config()

    def click_login(self):
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()

    def enter_email(self):
        email_input = self.driver.find_element(*self.EMAIL_INPUT)
        email_input.send_keys(self.config['email_peserta'])

    def enter_password(self):
        password_input = self.driver.find_element(*self.PASSWORD_INPUT)
        password_input.send_keys(self.config['password_peserta'])

    def click_masuk(self):
        login_button = self.driver.find_element(*self.BUTTON_MASUK)
        login_button.click()

    def login(self):
        self.open(self.config['base_url'])
        self.click_login()
        self.enter_email()
        self.enter_password()
        self.click_masuk()
        
