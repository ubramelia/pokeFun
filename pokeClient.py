import json
import requests

class PokeClient:
    """idk what im doing in this class yet."""
    def __init__(self, userID, oauthtoken):
        self._userID = userID
        self._oauthtoken = oauthtoken

    def _get_info_evolution(self, testability):
        """This method takes pokemon ability name then performs a get request to return a json file of poke info on it."""
        response = requests.get(
            url = f"https://pokeapi.co/api/v2/ability/{testability}/",
            headers = {
                "Content-Type": "application/json"
            }
        )
        
        data = response.json()
        return data