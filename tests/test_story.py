'''
Program: Choose your own adventure
Author: Bernard Paul
Purpose: this file will be the test for the player
Date:10/29/26

'''
import pytest

from story import get_next_scene, get_scene, the_ending

def test_get_scene():
    """this will make sure that a scene is gotten"""

    scene = get_scene("start") #grabs the starting scene
    assert "description" in scene

def test_get_next_scene():
    """making sure that the next scene is properly grabbed"""

    assert get_next_scene("start", "1") == "Light"

    assert get_next_scene("start", "2") == "Birds"

def test_wrong_choice():
    """ if the player makes a choice that isnt listed then it will raise an error"""
    with pytest.raises(ValueError):
        get_next_scene("start", "67") #purposely wrong choice to test 

        