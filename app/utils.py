import requests
from .config import Config

def get_pokemon_data(name):
    response = requests.get(f"{Config.POKEAPI_URL}pokemon/{name}")
    if response.status_code == 200:
        return response.json()
    return None
