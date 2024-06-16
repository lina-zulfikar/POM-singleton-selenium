from selenium.webdriver.common.by import By
from utils import driver_manager
from utils import config_manager

DriverManager = driver_manager.DriverManager

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver = DriverManager.get_driver()
        self.BUTTON_LOGIN = (By.XPATH, '//a[normalize-space()="Login"]')
        self.EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Email"]')
        self.PASSWORD_INPUT = (By.XPATH, '//input[@placeholder="Password"]')
        self.BUTTON_MASUK = (By.XPATH, '//button[normalize-space()="Masuk"]')

    def login(self, email, password):
        self.driver.find_element(*self.BUTTON_LOGIN).click()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.BUTTON_MASUK).click()