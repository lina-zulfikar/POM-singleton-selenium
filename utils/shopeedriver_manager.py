from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

class DriverManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DriverManager, cls).__new__(cls)
            cls._instance.driver = None
        return cls._instance
    
    def get_driver(self):
        if self.driver is None:
            self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
            self.driver.maximize_window() 
        return self.driver

    def close_driver(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None