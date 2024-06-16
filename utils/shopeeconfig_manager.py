class ConfigManager:
    _instance = None
    config_data = {
        "base_url": "http://127.0.0.1:8080",
        "email_admin": "linazulfikar99@gmail.com",
        "password_admin": "Testingautomation",
        "email_peserta": "linazulfikar16@gmail.com",
        "password_peserta": "Testingpeserta"
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
        return cls._instance

    @classmethod
    def get_config(cls):
        return cls.config_data
