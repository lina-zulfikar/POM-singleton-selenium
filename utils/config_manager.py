class ConfigManager:
    _instance = None
    config_data = {
        "base_url": "http://127.0.0.1:8080",
        "email": "linazulfikar99@gmail.com",
        "password": "Testingautomation"
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
        return cls._instance

    @classmethod
    def get_config(cls):
        return cls.config_data

# class ConfigManager:
#     _instance = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(ConfigManager, cls).__new__(cls)
#             cls._instance.base_url = "http://127.0.0.1:8080"
#             cls._instance.email = "linazulfikar99@gmail.com"
#             cls._instance.password = "Testingautomation"
#         return cls._instance



# class ConfigManager:
#     _instance = None
#     _is_loaded = False

#     def __new__(cls, *args, **kwargs):
#         if not cls._instance:
#             cls._instance = super(ConfigManager, cls).__new__(cls)
#         return cls._instance

#     def __init__(self):
#         if not self._is_loaded:
#             # Load the configuration settings from a file or environment variables here
#             # For example, set the base URL and any other global settings
#             self.base_url = "http://127.0.0.1:8080"
#             self.email = "linazulfikar99@gmail.com"
#             self.password = "Testingautomation"
#             # Set _is_loaded to True so initialization does not happen again
#             self._is_loaded = True

#     # ... Other methods related to configuration can be added here

# # Usage:
# config = ConfigManager()
# print(config.base_url)  