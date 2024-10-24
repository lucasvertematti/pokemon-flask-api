import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    POKEAPI_URL = "https://pokeapi.co/api/v2/"
