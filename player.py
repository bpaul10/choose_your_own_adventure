"""
program: choose your own adventure
Author: Bernard Paul
Purpose: This will the be character and player class for the game
Sources: Python crash course book using the python library 
10/23/26
"""

class Character:
    #this will be the character for the game
    def __init__(self, name):
        #this initializing the character with a name attached to it 
        self.name = name

    def opener (self):
        #creating an opening line to the player 
        return f"Salutations I am {self.name}."


