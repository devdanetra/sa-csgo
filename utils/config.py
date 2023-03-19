import json

CONFIG_DIRECTORY_PATH = './test/config'
CONFIG_FILE_NAME = 'config'


class ConfigManager:
    data = '';

    @staticmethod
    def get(name):
        with open(f"{CONFIG_DIRECTORY_PATH}/{CONFIG_FILE_NAME}.json", "r") as file:
            data = json.load(file)
            return data['config'][name]

    @staticmethod
    def getEntire(name):
        with open(f"{CONFIG_DIRECTORY_PATH}/{CONFIG_FILE_NAME}.json", "r") as file:
            return json.load(file)

    @staticmethod
    def setProperty(name, value):
        data = ConfigManager.getEntire()
        data['config'][name] = value
        
        with open(f"{CONFIG_DIRECTORY_PATH}/{CONFIG_FILE_NAME}.json", "w") as file:
            json.dump(data,file)
            return value