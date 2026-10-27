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
                "next scene": "",
            },
            "2":{
                "info": "go towards the bird noises",
                "next scene": "",
            },            
        },

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

