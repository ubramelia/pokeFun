# import the json file
import json

# Opening JSON file
with open('logs\pokeInfo.json') as json_file:
	data = json.load(json_file)

	# for reading nested data [0] represents the index value of the list
	print(data['pokemon'][0])
	
	# for printing the key-value pair of
	# nested dictionary for loop can be used
	print("\nPrinting nested dictionary as a key-value pair\n")
	for i in data['pokemon']:
		print("Is the ability hidden?", i['is_hidden'])
        print("Pokemon with ability: ", i['name'])
        print("Learn more about them at:", i['url'])
		print("Slot: ", i['slot'])
        print()
