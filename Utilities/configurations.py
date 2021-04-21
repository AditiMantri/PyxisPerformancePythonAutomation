import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('Utilities/properties.ini')
    return config
