"""
Program: choose your own adventure 
Author: Bernard Paul
Purpose:main.py this file will be the main hub for the adventure loop 
Sources: Python crash course book using the python library 
10/24/26
"""
from player import Player
from story import STORY, get_scene, get_next_scene, the_ending
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

def gameplay(player):
    """this is going to run the story in a loop unless player quits or finishes"""
    print("Adventure started")

    while True:
        scene = get_scene(player.current_scene) #grabs what the scene is from player object
        show_scene(player.current_scene)

        if the_ending(player.current_scene):#checks if the story ended
            print("congratualations you have completed the adventure")
            return

        print("if you want to save your game press S if you want to quit hit Q")

        options = set(scene["choices"]) | {"S","s","Q","q"} #list of what is an acceptable input
        choice = get_choice(options).upper() #gets the user input and converts to uppercase

        if choice == "Q":
            print("Bye")
            return
        if choice == "S":
            if save_game(player):
                print("you have saved")
            return

        selected_option = scene["choices"][choice]
        choice_text = selected_option["text"]
        next_scene= get_next_scene(player.current_scene, choice)
        player.make_choice(choice_text, next_scene)


def main():
    """this will be the game starter and handle the main menu selection"""

    while True:
        menu_choice = show_menu()

        if menu_choice == "1":
            player = create_player()
            gameplay(player)

        elif menu_choice == "2":
            player = load_game()

            if player is None:
                print("you dont have a save file")
            else:
                gameplay(player)

        elif menu_choice == "3":
            print("leaving game")
            break

if __name__ == "__main__":
    main()