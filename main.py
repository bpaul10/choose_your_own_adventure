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
    scene = get_scene(scene_name)
    print(f"\n{'-'*50}")
    print(scene["title"])