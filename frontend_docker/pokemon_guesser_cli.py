import sys
import os
import requests
from random import randint
import urllib.request

#api_url = os.environ.get('API_URL')
api_url = "http://127.0.0.1:8000/"

def get_pokemon_name(index):
    url = api_url + "pokemon_name/" + str(index)
    response = requests.get(url)
    return response.json()["name"]

def get_pokemon_sprite_url(index,answer):
    if answer == True:
        url = api_url + "pokemon_sprite_for_answer/" + str(index)
    else:
        url = api_url + "pokemon_sprite_for_guesser/" + str(index)
    response = requests.get(url)
    img_url = response.json()["link"]    
    return img_url

def get_pokemon_moves(index):
    url = api_url + "pokemon_moves/" + str(index)
    response = requests.get(url)
    return response.json()["moves"]

def get_pokemon_species_flavor_text(index):
    url = api_url + "pokemon_species_flavor_text/" + str(index)
    response = requests.get(url)
    return response.json()["text"]

def save_sprite(url):
    filename = url.split('/')[-1]
    urllib.request.urlretrieve(url, filename)
    return filename

def show_image(index,answer):
    url = get_pokemon_sprite_url(index,answer)
    filename = save_sprite(url)
    os.system(f"tiv ./{filename}")
    return filename

def delete_image(filename):
    os.system(f"rm {filename}")

if __name__ == "__main__":
    GAME_MENU = True
    while GAME_MENU:
        print("======Welcome to Pokeman Guessing Game=====")
        r_num = randint(1,151)
        name = get_pokemon_name(r_num)
        filename = show_image(r_num,False)
        user_input = input("Please guess the name of the pokemon: ")
        while name != user_input.lower():
            user_input = input("Wrong Answer! Please try again or type a to get the answer: ")
            if user_input != "a":
                continue
            else:
                show_image(r_num,True)
                print("The Answer is " + name)
                print("\n")
                break
        if name == user_input.lower():
            show_image(r_num,True)
            print("Well done! You are a Pokemon Expert!")
            print("\n")
        user_input2 = input("Press Enter to continue or q to quit:")
        if user_input2 == "q":
            delete_image(filename)
            sys.exit()
        else:
            delete_image(filename)
            print("\n")