from flask import Blueprint, jsonify, request
import requests
import random
from .auth import token_required
from .config import Config
from .utils import get_pokemon_data

api_routes = Blueprint('api', __name__)

# Obtém o tipo do Pokémon pelo nome
@api_routes.route('/pokemon/type/<name>', methods=['GET'])
@token_required
def get_pokemon_type(name):
    data = get_pokemon_data(name)
    if not data:
        return jsonify({'error': 'Pokemon not found'}), 404

    return jsonify({'name': name, 'types': [t['type']['name'] for t in data['types']]})

# Obtém um Pokémon aleatório de um tipo específico
@api_routes.route('/pokemon/random/<type>', methods=['GET'])
@token_required
def get_random_pokemon_by_type(type):
    response = requests.get(f"{Config.POKEAPI_URL}type/{type}")
    if response.status_code != 200:
        return jsonify({'error': 'Type not found'}), 404
    
    pokemons = response.json()['pokemon']
    random_pokemon = random.choice(pokemons)['pokemon']
    return jsonify({'random_pokemon': random_pokemon})

# Obtém o Pokémon com o nome mais longo de um tipo específico
@api_routes.route('/pokemon/longest/<type>', methods=['GET'])
@token_required
def get_longest_name_pokemon(type):
    response = requests.get(f"{Config.POKEAPI_URL}type/{type}")
    if response.status_code != 200:
        return jsonify({'error': 'Type not found'}), 404
    
    pokemons = response.json()['pokemon']
    longest_name_pokemon = max(pokemons, key=lambda p: len(p['pokemon']['name']))['pokemon']
    return jsonify({'longest_name_pokemon': longest_name_pokemon})
