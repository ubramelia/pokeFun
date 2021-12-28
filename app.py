import json
import configparser

config = configparser.ConfigParser()
from pokeClient import PokeClient

config.read('config.ini')
"""[DEFAULT] key pairs from config.ini file"""
username = config['DEFAULT']['USERNAME']
userID = config['DEFAULT']['USERID']
"""[TOKENS] key pairs from config.ini file"""
oauthtoken = config['TOKENS']['OAUTHTOKEN']
"""[USERINPUT] key pairs from config.ini file"""
testpokemon = config['USERINPUT']['TESTPOKEMON']
testability = config['USERINPUT']['TESTABILITY']
testitemname = config['USERINPUT']['TESTITEMNAME']

pokeclient = PokeClient(userID, oauthtoken)
pokeinfo = pokeclient._get_info_pokename(testpokemon)

#TODO: add command to create folders
with open('./logs/pokeInfo.json', 'w') as outfile:
    json.dump(pokeinfo, outfile)

# TODO: 