import logging

class Logger:
    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = logging.getLogger("SeleniumTesting")
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            cls._instance.addHandler(handler)
            cls._instance.setLevel(logging.INFO)
        return cls._instance
