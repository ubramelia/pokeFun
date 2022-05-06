from cgi import test
import json
import configparser
from platform import node
from tkinter import Y

config = configparser.ConfigParser()

from pokeClient import PokeClient
from graph import Graph
from collections import defaultdict

config.read('config.ini')
"""[DEFAULT] key pairs from config.ini file"""
username = config['DEFAULT']['USERNAME']
userID = config['DEFAULT']['USERID']
"""[TOKENS] key pairs from config.ini file"""
oauthtoken = config['TOKENS']['OAUTHTOKEN']
"""[USERINPUT] key pairs from config.ini file"""
testpokemon = config['USERINPUT']['TESTPOKEMON']
#testability = config['USERINPUT']['TESTABILITY']
#testability2 = config['USERINPUT']['TESTABILITY2']
testitemname = config['USERINPUT']['TESTITEMNAME']
location = config['USERINPUT']['LOCATION']

pokeclient = PokeClient(userID, oauthtoken)

print("\nHi! I'm called The Pokedex.")
print("I know everything there is to know about Pokemon, ESPECIALLY pokemon abilities.\n")
print("In fact, if you tell me your 2 favorite Pokemon abilities, I can give you a list of all the Pokemon that have only 1 of the abilities AND which Pokemon have BOTH abilities.\n\n")
userAnswer = input("Wanna try me out? Answer Y or N .\n")
tryCounter = 0

while userAnswer != None:
    if userAnswer == "Y":
        testability = input("\n\nGreat :) Please enter the name of a Pokemon's ability below. \n (P.S. If it contains any spaces, add a dash where the space would be, instead.  ie: \"lightning-rod\" instead of \"lightning rod\".\n")
        testability2 = input("\nThat's a great one! Please enter one more below.\n")
        break
    elif userAnswer == "N":
        if tryCounter == 0:
            userAnswer = input("\n...please? I have no friends since I am a python program so I really need someone to play with.\n")
        elif tryCounter == 1:
            userAnswer = input("\nPLEASE?!? IT WILL BE SO QUICK\n")
        elif tryCounter == 2:
            userAnswer = input("\nI'M BEGGING YOU!\n")
        else:
            print("\nFine, then.  Close out of this program and go away.")
            break
        tryCounter += 1
    else:
        userAnswer = input("I don't understand what you're saying. Please respond with \"Y\" or \"N\".\n")

#Get info on testability
pokeinfo = pokeclient._get_info_evolution(testability)
with open('./logs/pokeInfo.json', 'w') as outfile:
    json.dump(pokeinfo, outfile)

#Get info on testability2
pokeinfo2 = pokeclient._get_info_evolution(testability2)
with open('./logs/pokeInfo2.json', 'w') as outfile:
    json.dump(pokeinfo2, outfile)

#Create Dictionaries
pokeDict = {}
pokeDict2 = {}

#Parse json for ALL name of pokemon who can have abililites.
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
#print(dict_3)

for key in list(dict_3.keys()):
    Graph.addEdge(Graph.graph, key, dict_3[key])
#print(Graph.generate_edges(Graph.graph))

#More user interaction...
print(f'Alright, I have travelled across the land, searching far and wide for all the Pokemon that can have the {testability} or {testability2} abilities.\n')
print("I have compiled the information into a graph so that I can easily access it.")
print("I can give you give you 3 different types of information on it...\n")
print(f'1 - A list of all Pokemon that can have the {testability} ability.\n')
print(f'2 - A list of all Pokemon that can have the {testability2} ability\n.')
print(f'3 - A list of all Pokemon that can have either of these abilities.\n\n')
userAnswer = input("Would you like 1 , 2, or 3 ?\n")

if userAnswer == "1":
    print(f'\nAbility: {testability} \n')
    print(f"\nPokemon with Ability:")
    print(f'{pokeDict.keys()} \n')
elif userAnswer == "2":
    print(f'\nAbility: {testability2} \n')
    print(f"\nPokemon with Ability:")
    print(f'{pokeDict2.keys()} \n')
elif userAnswer == "3":
    print(Graph.generate_edges(Graph.graph))
    #for keys in list(dict_3.keys()):
    #    print(f'\nPokemon: {keys} \n Abilities: {Graph.graph[keys]}\n')
else:
    print("\nI don't understand. Please answer either with a single integer between 1 and 3.\n")

