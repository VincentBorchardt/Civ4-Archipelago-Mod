from CvPythonExtensions import *
from PyHelpers import *
from Popup import PyPopup

import BugOptions

import ArchipelagoStuff
import ArchipelagoData

# constants
gc = CyGlobalContext()
cyGame = CyGame()
cyMap = CyMap()
pyGame = PyGame()

LOCATION_TO_LOCATION_ID = {
    "TECH_ARCHIPELAGO1" : 1
}

# TODO move this into a "ArchipelagoConstants" file along with my various mapping dicts?
validGPs = [
    "UNITCLASS_SCIENTIST", "UNITCLASS_ENGINEER", "UNITCLASS_PROPHET", 
    "UNITCLASS_ARTIST", "UNITCLASS_MERCHANT", "UNITCLASS_GREAT_GENERAL", "UNITCLASS_GREAT_SPY"
]

# Should this be here? I don't know if this is persistent or not
checkedLocations = []

def sendLocationCheck(location_name):
    location_id = LOCATION_TO_LOCATION_ID[location_name]
    checkedLocations.append(location_id)
    messageDict = {"type" : "LocationChecks", "locations" : checkedLocations}
    dataDict = ArchipelagoStuff.sendAndReceiveData(messageDict, waitForRead=False)
    return dataDict



def checkIfArchipelagoTech(tech):
	
    tech_info = gc.getTechInfo(tech)
    
    # FLAVOR_ARCHIPELAGO is FlavorValue(8); currently hardcoded
    flavor_weight = tech_info.getFlavorValue(8)
    if flavor_weight > 0:
        tech_name = tech_info.getType()
        sendLocationCheck(tech_name)
        # Show something in the message log saying what you sent?
        ArchipelagoStuff.showPopup("This is an Archipelago Tech", ArchipelagoStuff.popupMessage)


def processGPArchipelagoBulb(unitId):
    CyInterface().addImmediateMessage(str(unitId), "")
    # 1. Grab the active player instance
    iPlayerId = gc.getGame().getActivePlayer()
    pPlayer = gc.getPlayer(iPlayerId)

    # 2. Extract the physical unit object using your unitID variable
    pUnit = pPlayer.getUnit(unitId)

    if pUnit and not pUnit.isNone():
        iUnitType = pUnit.getUnitType()
        iUnitClass = gc.getUnitInfo(iUnitType).getUnitClassType()
        szClassTypeStr = gc.getUnitClassInfo(iUnitClass).getType()
        if szClassTypeStr in validGPs:
            checkIndex = ArchipelagoData.archipelagoGPChecks.get(szClassTypeStr)
            if checkIndex is None:
                checkIndex = 1
            else:
                checkIndex += 1
            if checkIndex > ArchipelagoData.archipelagoMaxGPSanity:
                CyInterface().addImmediateMessage("AP Error: Cannot bulb location above GPSanity max", "")
                return False
            location_name = szClassTypeStr + "_" + str(checkIndex)
            CyInterface().addImmediateMessage(location_name, "")
            #sendLocationCheck(location_name)
            # TODO put the function that grabs what the next check for preview purposes here
            #ArchipelagoData.archipelagoGPChecks[szClassTypeStr] = checkIndex
            #ArchipelagoData.save()
            return True
    CyInterface().addImmediateMessage("Invalid unit selected for GP Bulb", "")
    return False
