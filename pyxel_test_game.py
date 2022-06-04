import pyxel
import os
import requests
import json
from random import randint
import urllib.request

api_url = "http://18.237.55.156:63375/"


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
    return filename


def add_letter(text):
    if pyxel.btnr(pyxel.KEY_A):
        text += "a"
    elif pyxel.btnr(pyxel.KEY_B):
        text += "b"
    elif pyxel.btnr(pyxel.KEY_C):
        text += "c"
    elif pyxel.btnr(pyxel.KEY_D):
        text += "d"
    elif pyxel.btnr(pyxel.KEY_E):
        text += "e"
    elif pyxel.btnr(pyxel.KEY_F):
        text += "f"
    elif pyxel.btnr(pyxel.KEY_G):
        text += "g"
    elif pyxel.btnr(pyxel.KEY_H):
        text += "h"
    elif pyxel.btnr(pyxel.KEY_I):
        text += "i"
    elif pyxel.btnr(pyxel.KEY_J):
        text += "j"
    elif pyxel.btnr(pyxel.KEY_K):
        text += "k"
    elif pyxel.btnr(pyxel.KEY_L):
        text += "l"
    elif pyxel.btnr(pyxel.KEY_M):
        text += "m"
    elif pyxel.btnr(pyxel.KEY_N):
        text += "n"
    elif pyxel.btnr(pyxel.KEY_O):
        text += "o"
    elif pyxel.btnr(pyxel.KEY_P):
        text += "p"
    elif pyxel.btnr(pyxel.KEY_Q):
        text += "q"
    elif pyxel.btnr(pyxel.KEY_R):
        text += "r"
    elif pyxel.btnr(pyxel.KEY_S):
        text += "s"
    elif pyxel.btnr(pyxel.KEY_T):
        text += "t"
    elif pyxel.btnr(pyxel.KEY_U):
        text += "u"
    elif pyxel.btnr(pyxel.KEY_V):
        text += "v"
    elif pyxel.btnr(pyxel.KEY_W):
        text += "w"
    elif pyxel.btnr(pyxel.KEY_X):
        text += "x"
    elif pyxel.btnr(pyxel.KEY_Y):
        text += "y"
    elif pyxel.btnr(pyxel.KEY_Z):
        text += "z"
    return text

        
def remove_letter(text):
    if text.split(':\n\n')[-1] != "":
        return text[:-1]
    else:
        return text

class App:

    def __init__(self):
        pyxel.init(180, 180, title="Pokemon Guesser Game")
        self.game_init()
        
        pyxel.run(self.update, self.draw)
        
    def game_init(self):
        r_num = randint(1,151)
        self.index = r_num
        self.restart = False
        self.hint1 = True
        self.imgw = 40
        self.imgh = 30
        self.imgx = 70
        self.imgy = 10
        self.txtx = 10
        self.txty = 80
        self.message = "Please guess the name of the pokemon\n(type h to get hint):\n\n"
        self.name = get_pokemon_name(r_num)
        self.filename = show_image(r_num,False)
        pyxel.image(0).load(0, 0, self.filename)

    def set_answer_image(self):
        self.filename = show_image(self.index,True)
        pyxel.image(0).load(0, 0, self.filename)
        self.imgw = 128
        self.imgh = 128
        self.imgx = 26
        self.imgy = 0
    
    def update(self):
        if pyxel.btnr(pyxel.KEY_0):
            os.remove(self.filename)
            quit()
            
    
    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.imgx, self.imgy, 0, 0, 0, self.imgw, self.imgh)
        
        self.message = add_letter(self.message)
        pyxel.text(self.txtx, self.txty, self.message, pyxel.COLOR_WHITE)
        
        if pyxel.btnr(pyxel.KEY_RETURN):
            if self.restart == False:
                guessed_name = self.message.split(':\n\n')[-1]
                if guessed_name == self.name:
                    self.set_answer_image()
                    self.txty = 130
                    self.message = f"Well done! It's {self.name}!\nYou are a pokemon expert!!\n\nPress enter to Continue, 0 to quit: "
                    self.restart = True
                elif guessed_name == "a":
                    self.set_answer_image()
                    self.txty = 130
                    self.message = f"The answer is {self.name}!!\n\nPress enter to Continue, 0 to quit: "
                    self.restart = True
                elif guessed_name == "h":
                    if self.hint1:
                        text = get_pokemon_species_flavor_text(self.index)
                        self.message = f"Hint 1:\n{text}\n\nPlease guess the pokemon's name\n(press h to get more hints):\n\n"
                        self.hint1 = False
                    else:
                        moves = get_pokemon_moves(self.index)
                        self.message = f"Hint 2:\nThe pokemon's {len(moves)} moves:\n"+"\n".join(f"{move}" for move in moves) + "\n\nPlease guess the pokemon's name\n(press a to get answer):\n\n"
                        self.hint1 = True

                else:    
                    self.message = f"Wrong Answer! Please try again\n\n(Type h get hint):\n\n"    
            else:
                os.remove(self.filename)
                self.game_init()

        if pyxel.btnr(pyxel.KEY_BACKSPACE):
            self.message = remove_letter(self.message)
App()