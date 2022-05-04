from fastapi import FastAPI
import requests
from pokemon_db import get_moves, get_name, get_species_flavor_text

app = FastAPI()


@app.get("/pokemon_sprite_for_guesser/{pokemon_id}")
def get_url(pokemon_id):
    api_url = "https://pokeapi.co/api/v2/pokemon/" + str(pokemon_id)
    #Get the data from the pokeapi 
    response = requests.get(api_url)
    link = response.json()["sprites"]["versions"]["generation-vii"]["icons"]["front_default"]
    return {'link': link}

@app.get("/pokemon_sprite_for_answer/{pokemon_id}")
def get_url(pokemon_id):
    api_url = "https://pokeapi.co/api/v2/pokemon/" + str(pokemon_id)
    #Get the data from the pokeapi 
    response = requests.get(api_url)
    link = response.json()["sprites"]["versions"]["generation-vii"]["ultra-sun-ultra-moon"]["front_default"]
    return {'link': link}

@app.get("/pokemon_name/{pokemon_id}")
def print_pokemon_name(pokemon_id):
    #Get the data from the database
    name = get_name(pokemon_id)
    return {'name': name}

@app.get("/pokemon_moves/{pokemon_id}")
def list_pokemon_moves(pokemon_id):
    #Get the data from the database
    moves = get_moves(pokemon_id)
    return {'moves': moves}

@app.get("/pokemon_species_flavor_text/{pokemon_id}")
def print_pokemon_species_flavor_text(pokemon_id):
    #Get the data from the database
    text = get_species_flavor_text(pokemon_id)
    return {'text': text}