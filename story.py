"""
program: choose your own adventure
Author: Bernard Paul
Purpose: this is the story of the game that will be played and 
will have the different branches of what the player can do 
Sources: Python crash course book using the python library 
10/23/26
"""

STORY = {
    """
    locations have their descriptions and title and then 
    choices that the player can choose from and the 
    outcome written in 
    """
    "forest":{ 
        "title": "Freaky Forest",
        "description": ("You have entered a forest with a bunch of freaky objects and animals"
                        "You must remain strong and determine what to do"
                        "You walk deeper into the forest and find a freak fork in the road. "
                        "It appears to go off into 2 sections one where light appears to be coming from the end"
                        "and then another one where there is a lot bird noises"
                     ),

        "choices": {
            "1":{
                "info": "Go towards the light",
                "next scene": "Light",
            },
            "2":{
                "info": "go towards the bird noises",
                "next scene": "Birds",
            },            
        },
        "ending" : False, 

    },

    "Birds":{ 
        "title": "Bird Attack!",
        "description": ("You walk towards the path where the bird noise is coming from"
        "Its dark and hard to see and you end up accidentally kicking one of the birds"
        "The bird screams in agaony and summons forth its fellow bird friends"
        "Now there is a flock of birds coming at your what will you do?"
                        
                     ),

        "choices": {
            "1":{
                "info": "try to fight the birds",
                "next scene": "Bird Fight",
            },
            "2":{
                "info": "run like your life depends on it because it truly does",
                "next scene": "Bird Run",
            },            
        },
        "ending" : False, 

    },
        "Bird Run":{ 
        "title": "RUN!",
        "description": ("You start booking it in the opposite direction but the birds only seem to be"
        "muiltiplying as if there is an infinite amount of them"
        "you try to keep going but you trip over a conviently placed stick and upon impact you wake up and find out it was all a dream."                  
                     ),

        "choices": {
            "1":{
                "info": "try to fight the birds",
                "next scene": "Bird Fight",
            },
            "2":{
                "info": "run like your life depends on it because it truly does",
                "next scene": "Bird Run",
            },            
        },
        "ending" : True, 

    },
    "Light":{ 
        "title": "The Light ",
        "description": ("You have walked towards the light interesting choice there buddy."
        "As you adventure deeper into the forest towards the light you come across what appears to be..."
        "Holy smokes whatcha know another fork in da road!"
        "You are starting to get really hungry at this point and it appears that there is some sort of fruit tree"
        "on one side while on the other side there seems to just be well more forest"
        "which path will you take?"
 
                     ),

        "choices": {
            "1":{
                "info": "Go towards the fruit trees",
                "next scene": "",
            },
            "2":{
                "info": "continue on the path with more forest",
                "next scene": "",
            },            
        },
        "ending" : False, 

    },
}

#Functions for scene management 

def get_scene(scene_name):
    #will get the scene from the story
    if scene_name not in STORY:
        raise ValueError (f"{scene_name} not in story ")
    return STORY(scene_name)


def get_next_scene(scene_name, choice):
    #will give the next scene and make sure it is real 

    scene = get_scene(scene_name)
    if choice not in scene["choices"]:
        raise ValueError(f"Invalid choiceL {choice}")
    return scene["choices"][choice]["next_scene"]

def the_ending(scene_name):
    """If the scene is ending this will be True"""
    return get_scene(scene_name)["ending"] #checks the value of the ending status 