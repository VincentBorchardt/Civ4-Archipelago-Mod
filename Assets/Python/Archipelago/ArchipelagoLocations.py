from CvPythonExtensions import *
from PyHelpers import *
from Popup import PyPopup

import BugOptions

import ArchipelagoStuff

# constants
gc = CyGlobalContext()
cyGame = CyGame()
cyMap = CyMap()
pyGame = PyGame()

TECH_TO_LOCATION_ID = {
    "TECH_ARCHIPELAGO1" : 1
}

# Should this be here? I don't know if this is persistent or not
checkedLocations = []

def checkIfArchipelagoTech(tech):
	
    tech_info = gc.getTechInfo(tech)
    
    # FLAVOR_ARCHIPELAGO is FlavorValue(8); currently hardcoded
    flavor_weight = tech_info.getFlavorValue(8)
    if flavor_weight > 0:
        tech_name = tech_info.getType()
        tech_id = TECH_TO_LOCATION_ID[tech_name]
        checkedLocations.append(tech_id)
        messageDict = {"type" : "LocationChecks", "locations" : checkedLocations}
        dataDict = ArchipelagoStuff.sendAndReceiveData(messageDict, waitForRead=False)
        # Show something in the message log saying what you sent?
        ArchipelagoStuff.showPopup("This is an Archipelago Tech", ArchipelagoStuff.popupMessage)
