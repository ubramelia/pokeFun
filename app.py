import json
import configparser

config = configparser.ConfigParser()
from pokeClient import PokeClient

from collections import defaultdict

config.read('config.ini')
"""[DEFAULT] key pairs from config.ini file"""
username = config['DEFAULT']['USERNAME']
userID = config['DEFAULT']['USERID']
"""[TOKENS] key pairs from config.ini file"""
oauthtoken = config['TOKENS']['OAUTHTOKEN']
"""[USERINPUT] key pairs from config.ini file"""
testpokemon = config['USERINPUT']['TESTPOKEMON']
testability = config['USERINPUT']['TESTABILITY']
testability2 = config['USERINPUT']['TESTABILITY2']
testitemname = config['USERINPUT']['TESTITEMNAME']
location = config['USERINPUT']['LOCATION']

pokeclient = PokeClient(userID, oauthtoken)

#Get info on testability
pokeinfo = pokeclient._get_info_evolution(testability)
with open('./logs/pokeInfo.json', 'w') as outfile:
    json.dump(pokeinfo, outfile)

#Get info on testability2
pokeinfo2 = pokeclient._get_info_evolution(testability2)
with open('./logs/pokeInfo2.json', 'w') as outfile:
    json.dump(pokeinfo2, outfile)

#Create Dictionary
pokeDict = {}
pokeDict2 = {}

#Parse json for ALL name of pokemon who can have testability
def appendPokeDict(pokeDict, pokeinfo, testability):
    pokeNum = -1
    firstPoke = pokeinfo['pokemon'][0]['pokemon']['name']
    pokeNumPoke = pokeinfo['pokemon'][pokeNum]['pokemon']['name']

    while pokeNumPoke != None:
        pokeName = pokeinfo['pokemon'][pokeNum]['pokemon']['name']    
        if pokeName == firstPoke:
            #print("The number is ", pokeNum)
            #print("The name is", pokeName)
            dictIndex = (pokeNum * -1) - 1
            if "pokeName" in pokeDict:
                pokeDict.setdefault(pokeName, []).append(testability)
            else:           
                pokeDict[pokeName] = testability
            break
        else:
            #print("The number is ", pokeNum)
            #print("The name is", pokeName)
            dictIndex = (pokeNum * -1) - 1
            if "pokeName" in pokeDict:
                pokeDict.setdefault(pokeName, []).append(testability)
            else:           
                pokeDict[pokeName] = testability
            pokeNum -= 1
    #example code: print("This is pokemon info", pokeinfo['pokemon_encounters'][1]['pokemon']['name'])

appendPokeDict(pokeDict, pokeinfo, testability)
#print(pokeDict)
appendPokeDict(pokeDict2, pokeinfo2, testability2)
#print(pokeDict2)

def mergeDictionary(pokeDict, pokeDict2):
   dict_3 = {**pokeDict, **pokeDict2}
   for key, value in dict_3.items():
       if key in pokeDict and key in pokeDict2:
               dict_3[key] = [value , pokeDict[key]]
   return dict_3

dict_3 = mergeDictionary(pokeDict, pokeDict2)
print(dict_3)