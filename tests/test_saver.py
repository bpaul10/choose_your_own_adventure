'''
Program: Choose your own adventure
Author: Bernard Paul
Purpose: this file will be the test for the saver
Date:10/30/26

'''
import json
from player import Player
from saver import save_game, load_game

def test_save_n_loader(tmp_path): #t path is tempoary path 
    s_path = tmp_path / "save_game.json" #makes json file in the file path 

    player = Player("Jeff") #made a player

    player.make_choice("Go towards the light", "Light") #having the player make the choice of the light 
    assert save_game(player, s_path) is True # save the player info and make sure it was saved correctly  
    loaded_player = load_game(s_path)#make sure the game is saved in the json file 

    assert loaded_player is not None #make sure the player is loaded
    assert loaded_player.name == "Jeff"# cgecking that the name is loaded correctly
    assert loaded_player.choices_made == ["Go towards the light"] #make sure the player choice saves correctly
    assert loaded_player.current_scene == "Light" #make sure the choice picked is saved correctly 

def test_load_fail_file(tmp_path):
    """making a load that is a missing file so that it will have a return of none"""
    #makes json file in the file path 
    s_path = tmp_path / "save_game.json"
    assert load_game(s_path) is None #makinng sure that the load of hte missing file is a none


def test_load_corup_file(tmp_path):
    """what happens if the json file is corrupted"""
    s_path = tmp_path / "c.json" 

    s_path.write_text("invalid json}", encoding = "utf-8")# this is writing invalid json text to the file to have a corruption

    #checks that the program does the corrupt file by returning done 
    assert load_game(s_path) is None