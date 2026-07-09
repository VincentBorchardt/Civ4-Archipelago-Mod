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

# Should this be here? I don't know if this is persistent or not


def sendLocationCheck(location_name):
    location_id = LOCATION_TO_LOCATION_ID[location_name]
    ArchipelagoData.archipelagoCheckedLocations.append(location_id)
    ArchipelagoData.save()
    return sendStoredLocations()
    

def sendStoredLocations():
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

def cannotResearchTechsanityGate(ePlayer, eTech):
    pPlayer = gc.getPlayer(ePlayer)
    
    # Identify whether the technology being queried belongs to our custom Faux track
    # Using your working hardcoded flavor value method for execution safety
    isFauxTech = (gc.getTechInfo(eTech).getFlavorValue(8) > 0)

    # --- RULE GROUP 1: THE AI PLAYERS ---
    if not pPlayer.isHuman():
        if isFauxTech:
            return True  # HARD BLOCK: AI can NEVER research faux archipelago checks
        return False     # ALLOW: AI always researches standard vanilla paths

    # --- RULE GROUP 2: THE HUMAN PLAYER ---
    if ArchipelagoData.archipelagoTechSanityEnabled:
        if isFauxTech:
            return False # ALLOW: Human researches Faux techs when option is active
        return True      # HARD BLOCK: Human can never research vanilla paths directly
    else:
        # If Techsanity is completely turned off for this match session
        if isFauxTech:
            return True  # HARD BLOCK: Hide faux tracks completely
        return False     # ALLOW: Human plays normal vanilla game rules layout



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

