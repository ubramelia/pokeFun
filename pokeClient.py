import json
import requests

class PokeClient:
    """idk what im doing in this class yet."""
    def __init__(self, userID, oauthtoken):
        self._userID = userID
        self._oauthtoken = oauthtoken

    def _get_info_pokename(self, pokename):
        """This method takes pokemon name then performs a get request to return a json file of poke info."""
        response = requests.get(
            url = f"https://pokeapi.co/api/v2/pokemon/{pokename}/",
            headers = {
                "Content-Type": "application/json"
            }
        )
        
        data = response.json()
        return data