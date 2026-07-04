from CvPythonExtensions import *
from PyHelpers import *
from Popup import PyPopup

import BugOptions

import ArchipelagoStuff
import ArchipelagoData
from ArchipelagoConstants import *

# constants
gc = CyGlobalContext()
cyGame = CyGame()
cyMap = CyMap()
pyGame = PyGame()

LOCATION_TO_LOCATION_ID = {
    "TECH_ARCHIPELAGO1" : 1
}


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

def processTechLocationCheck(pPlayer, iTeam, eTech, szTechType):
    pTeam = gc.getTeam(iTeam)
    
    tech_data = TECH_LOCATION_MAP.get(szTechType)
    if not tech_data:
        return
        
    location_name = tech_data["location"]
    
    # CRITICAL FIX: Check if we already received this item from the multiworld server
    # We scan the persistence cache array to see if this tech's identifier string is already owned.
    bAlreadyOwnedFromServer = False
    for item_name in ArchipelagoData.archipelagoReceivedItems.itervalues():
        if item_name == szTechType:
            bAlreadyOwnedFromServer = True
            break

    if bAlreadyOwnedFromServer:
        # If we already own it, DO NOT strip the tech away!
        # Just give the player a message that they found a location check they already had the item for.
        CyInterface().addImmediateMessage("Location Check Found: " + location_name, "")
    else:
        # If we don't own it yet, strip it away normally to enforce Techsanity lockouts
        pTeam.setHasTech(eTech, False, pPlayer.getID(), False, False)
        CyInterface().addImmediateMessage("Research Intercepted! Sent Check: " + location_name, "")

    # Transmit the location check to your client socket smoothly
    # sendLocationCheck(location_name)

def validateGPCheck(unitId):
    """Pure validation function with NO gameplay mutations (No unit killing!)."""
    pPlayer = gc.getPlayer(gc.getGame().getActivePlayer())
    pUnit = pPlayer.getUnit(unitId)

    if pUnit and not pUnit.isNone():
        szClassTypeStr = gc.getUnitClassInfo(gc.getUnitInfo(pUnit.getUnitType()).getUnitClassType()).getType()
        if szClassTypeStr in VALID_GP_TYPES:
            checkIndex = ArchipelagoData.archipelagoGPChecks.get(szClassTypeStr, 0) + 1
            if checkIndex <= ArchipelagoData.archipelagoMaxGPSanity:
                return True
    return False

def executeGPArchipelagoBulb(pUnit):
    """Executes the state change and eliminates the unit safely inside the gameplay tick."""
    szClassTypeStr = gc.getUnitClassInfo(gc.getUnitInfo(pUnit.getUnitType()).getUnitClassType()).getType()
    
    checkIndex = ArchipelagoData.archipelagoGPChecks.get(szClassTypeStr, 0) + 1
    location_name = szClassTypeStr + "_" + str(checkIndex)
    
    # 1. Update State & Save
    ArchipelagoData.archipelagoGPChecks[szClassTypeStr] = checkIndex
    ArchipelagoData.saveData()
    
    # 2. Trigger Server Check Communication
    # sendLocationCheck(location_name)
    
    # 3. Safely kill the unit!
    pUnit.kill(True, -1)
    CyInterface().addImmediateMessage("Sacrificed Great Person for location: " + location_name, "")

