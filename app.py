import configparser

config = configparser.ConfigParser()

config.read('config.ini')
"""[DEFAULT] key pairs from config.ini file"""
username = config['DEFAULT']['USERNAME']
"""[TOKENS] key pairs from config.ini file"""
oauthtoken = config['TOKENS']['OAUTHTOKEN']
"""[USERINPUT] key pairs from config.ini file"""
testpokemon = config['USERINPUT']['TESTPOKEMON']
testability = config['USERINPUT']['TESTABILITY']
testitemname = config['USERINPUT']['TESTITEMNAME']

print(f"{username}")