"""
program: choose your own adventure
Author: Bernard Paul
Purpose: This will the be character and player class for the game
Sources: Python crash course book using the python library 
10/23/26
"""

class Player():
    """the actual player of the game and 
    how the adventure will be tracked"""
    def __init__(self, name, current_scene ="start" ):
        """initializing the player with the
        name and what scene they are going to be starting in"""
        self.name = name
        self.current_scene= current_scene
        self.choices_made = [] #keeping track with a list 

    def make_choice (self, choice, next_scene):
        """will keep track of a choice and then tell 
        the program what the next scene will be"""
        self.choices_made.append(choice) #adds the choice to the list of choices made
        self.current_scene = next_scene #updates current scene

    def send_to_dict(self):
        """ return the player  data for the json file """
        return{
            "name": self.name, 
            "current_scene": self.current_scene, 
            "choices_made": self.choices_made, 
        }

    def from_dict(cls, data): #creates object

        return cls( #making the instance of the class 
                name = data['name'], #grabs name from the dictonary 
                current_scene=data["current_scene"] #gets the scene from the dictonary 

            ).restore_choices(data.get("choices_made", [])) #brings back the saved choices from the list
    def restore_choices(self, choices):
        """will bring pback the players previous choices from list"""
        self.choices_made= list(choices) #takes the player and then its attribute being th choices made and then updates them 

        return self

class Character:
    #this will be the character for the game
    def __init__(self, name):
        #this initializing the character with a name attached to it 
        self.name = name

    def opener (self):
        #creating an opening line to the player 
        return f"Salutations I am {self.name}."


