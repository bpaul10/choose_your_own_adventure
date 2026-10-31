"""
program: choose your own adventure
Author: Bernard Paul
Purpose: saves the game to a python file 
that can be read 
Sources: Python crash course book using the python library
used chapter 10 of book for pathlib library  
10/23/26
"""

import json  
#pathlib works with the file paths and directories 
from pathlib import Path 
#import player class to have the game save data
from player import Player 


#delcare the default save path for the game 
Default = Path("saves/save_game.json") 


def save_game(player, file_path = Default):
    """ makes a json file nd writes in it where 
    the player is at"""

    path = Path(file_path)

    try:
        #will make the file if it isnt made
        path.parent.mkdir(parents=True, exist_ok=True)

        with path.open("w", encoding="utf-8") as save_file:
            #saves the players data into the tile 
            json.dump(player.send_to_dict(), save_file, indent=4)

        return True #if it happens it will return the boolean

    #handles error that might happen when the data cant be made into a json
    except(TypeError, ValueError) as error:
        print(f"couldnt save the save the error is {error}")

        return False

def load_game( file_path = Default):
    """
    will load the player prgogress from the json file 
    """

    path = Path(file_path) #file path conversion making it into an object

    try:
        #opening save file with the read mode and the utf-8 is encoding 
        with path.open("r", encoding = "utf-8")as save_file:


            data = json.load(save_file) #reading the json data and converting it into python data

        #this will make sure that the loaded data is a dictonary 
        if not isinstance(data, dict):
            raise ValueError("not a json object")

        #getting the name, current scene, and choices from the data
        name = data.get("name")
        current_scene =data.get("current_scene")
        choices = data.get("choices_made", [])
        #making the player object again using the information from the json file 
        player = Player.from_dict(data)
        return player

    #errors that may occur is handled with this 
    except (KeyError, TypeError, ValueError) as error:
        print(f"the game couldnt be loaded this is the error:{error}")
        return None
    except json.JSONDecodeError:
        return None
    except FileNotFoundError:
        return None