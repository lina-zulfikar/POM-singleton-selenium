from selenium import webdriver
from selenium.webdriver.firefox.service import Service

class DriverManager:
    _instance = None

    @classmethod
    def get_driver(cls):
        if cls._instance is None:
            s = Service(executable_path=r'C:\Program Files\Mozilla Firefox\firefox.exe')
            cls._instance = webdriver.Firefox(service=s)
            cls._instance.maximize_window()
        return cls._instance
    
# from selenium import webdriver

# class DriverManager:
#     _instance = None

#     @classmethod
#     def get_driver(cls):
#         if cls._instance is None:
#             options = webdriver.ChromeOptions()
#             # Set any options you like
#             cls._instance = webdriver.Firefox(executable_path=r'C:\Program Files\Mozilla Firefox\firefox.exe', options=options)
#             cls._instance.maximize_window()
#         return cls._instance