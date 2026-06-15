from CvPythonExtensions import *
from PyHelpers import *
from Popup import PyPopup

import BugOptions

import socket
import errno

# TODO NEED TO EVENTUALLY IMPLEMENT A SAFE UNPICKLER!!!
import pickle

import ArchipelagoStuff

# constants
gc = CyGlobalContext()
cyGame = CyGame()
cyMap = CyMap()
pyGame = PyGame()

TECH_TO_LOCATION_ID = {
    "TECH_ARCHIPELAGO1" : 1
}

def checkIfArchipelagoTech(tech):
	
	tech_info = gc.getTechInfo(tech)
    
	# FLAVOR_ARCHIPELAGO is FlavorValue(8); currently hardcoded
	flavor_weight = tech_info.getFlavorValue(8)
        if flavor_weight > 0:
                ArchipelagoStuff.showPopup("This is an Archipelago Tech", ArchipelagoStuff.popupMessage)
