"""
Program: choose your own adventure 
Author: Bernard Paul
Purpose:main.py this file will be the main hub for the adventure loop 
Sources: Python crash course book using the python library 
10/24/26
"""

#importing the player class to crreate and manage the player
from player import Player
#importing functions  and the story data this is used to show the scenes for adventure
from story import STORY, get_scene, get_next_scene, the_ending
#importing functions that are used to save and load the game
from saver import save_game, load_game

def show_scene(scene_name):
    #creating a cleaner way to display the scene information 
    scene = get_scene(scene_name) #intended use is to get the name from the story class
    print(f"\n{'-'*50}") #use as a seperator for clarity
    print(scene["title"]) #grabs title from scene dictonary 
    print(scene["description"]) #gives the information of that scene
    for choice, details in scene["choices"].items():
        print(f"{choice} {details['info']}")



def get_choice(valid_choice):
    """will ask for a choice from the player of what to do next"""
  
    while True: #keeps asking the playuer to provide answer until a valid choice is put
        choice = input("\nWhat is your choice:")

        #if the choice matches one of the options then it will reutnr it 
        if choice in valid_choice: 
            return choice

        print("You did not pick a choice from the options, please selected one of the ones listed please.")


def create_player ():
    """this will ask the user what the name of their player will be"""

    while True: #loop to keep asking the player for a name 
        name = input("what shall I call you?")

        #making an reutrning the player object only if the name was put in
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

    return get_choice({"1", "2"}) #obtaining and reutrning player menu

def gameplay(player):
    """this is going to run the story in a loop unless player quits or finishes"""
    print("Adventure started")

    while True:
        scene = get_scene(player.current_scene) #grabs what the scene is from player object
        show_scene(player.current_scene) #shows title of current scene

        if the_ending(player.current_scene):#checks if the story ended
            print("congratualations you have completed the adventure")
            return

        print("if you want to save your game press S if you want to quit hit Q")

        options = set(scene["choices"]) | {"S","s","Q","q"} #list of what is an acceptable input
        choice = get_choice(options).upper() #gets the user input and converts to uppercase

        if choice == "Q": #will end the game 
            print("Bye")
            return
        if choice == "S":# will save the players progress
            if save_game(player):
                print("you have saved")
            return

        #gets information that is from the players selected story option
        selected_option = scene["choices"][choice]
        #will store the text of the players decision
        choice_text = selected_option["info"]
        #gets the next scene from the current scene
        next_scene= get_next_scene(player.current_scene, choice)
        #updates plyaers choice history
        player.make_choice(choice_text, next_scene)


def main():
    """this will be the game starter and handle the main menu selection"""

    while True:
        menu_choice = show_menu()  

        #starts a new adventure for the player
        if menu_choice == "1":
            player = create_player()
            gameplay(player)

        #pulls the information from a save file and keeps that adventure going
        elif menu_choice == "2":
            player = load_game()

            if player is None: #tells the player if there is no save file 
                print("you dont have a save file")
            else:
                gameplay(player)

        #exits the program
        elif menu_choice == "3":
            print("leaving game")
            break

if __name__ == "__main__":
    main()