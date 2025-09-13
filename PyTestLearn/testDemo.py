import configparser
import os


print(os.getcwd())
filepath = "../config/environment.ini"
# filepath = os.path.abspath(filepath)

configManager = configparser.ConfigParser ()
configManager.read(filepath)
print(configManager.sections())
print(configManager['Module2']['keyB'])