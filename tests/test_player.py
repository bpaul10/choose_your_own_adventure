'''
Program: Choose your own adventure
Author: Bernard Paul
Purpose: this file will be the test for the player
Date:10/29/26

'''

from player import Character, Player

def test_character_intro():
    """making sure that the character can give its intro"""
    character = Character("Jeff")

    #making sure that the opener returns the right information
    assert character.opener() == f"Salutations I am Jeff."

# this is a test to make sure that the class initalizes with the values it is suppose to 
def test_player_init():
    player = Player("Jeff") #creating a new player named jeff
    assert player.name == "Jeff" #make sure that playyer name is correct
    assert player.current_scene == "start" #making sure the player starts at the start scene

    #make sure the list is empty when it starts
    assert player.choices_made == []

def test_player_choice_making():
    """making sure that the players progress is updating"""
    player= Player("Jeff") #makes the jeff character

    player.make_choice("Go towards the light", "Light") #simulation of what the player choices are 

    assert player.current_scene == "Light" #making sure that the scene is now light 
    assert player.choices_made ==["Go towards the light"]#make sure that the playuer choice is being saved
