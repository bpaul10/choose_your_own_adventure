"""
Program: choose your own adventure 
Author: Bernard Paul
Purpose:main.py this file will be the main hub for the adventure loop 
Sources: Python crash course book using the python library 
10/24/26
"""
from player import Player
from story import STORY, get_scene
from saver import save_game, load_game

def show_scene(scene_name):
    #creating a cleaner way to display the scene information 
    scene = get_scene(scene_name) #intended use is to get the name from the story class
    print(f"\n{'-'*50}") #use as a seperator for clarity
    print(scene["title"]) #grabs title from scene dictonary 


def get_choice(valid_choice):
    """will ask for a choice from the player of what to do next"""
    while True:
        choice = input("\nWhat is your choice:")

        if choice in valid_choice:
            return choice

        print("You did not pick a choice from the options, please selected one of the ones listed please.")


def create_player ():
    """this will ask the user what the name of their player will be"""
    while True:
        name = input("what shall I call you?")
        if name:
            return Player(name)
        print("You gotta have a name!")

def show_menu():
    """"will display the menu of what the player can do and the description of the game"""
    print("\n" + "-"*50)
    print("The Adventure")
    print("-"*45)
    print("1- Start a new adventure")
    print("2- continue your save file")
    print("3- Exit")
    print("Choose from the options please")

    return get_choice({"1", "2"})

