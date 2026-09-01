from CvPythonExtensions import *
import CvUtil
from PyHelpers import *
from Popup import PyPopup

import BugOptions
#import BugData

import ArchipelagoStuff
import ArchipelagoData
from ArchipelagoConstants import *

# constants
gc = CyGlobalContext()
cyGame = CyGame()
cyMap = CyMap()
pyGame = PyGame()


def receiveItems():
    messageDict = {"type":"ReceiveItems"}
    dataDict = ArchipelagoStuff.sendAndReceiveData(messageDict, waitForRead=True)
    if dataDict is None:
        ArchipelagoStuff.showPopup("Connection Error", "No Packet Received From receiveItems")
    # confirmed to have "cmd" in sendAndReceiveData
    elif dataDict.get("cmd") == "ReceiveItems":
        items = dataDict["items"]
        for item in items:
            item_index = item["index"]
            item_name = item["name"]
            player_name = item["player"]
            if ArchipelagoData.archipelagoReceivedItems.get(item_index) == item_name:
                continue  # already received item
            if 0 < item["item_id"] <= 100: # it is a tech
                grantTech(item_name)
                CyInterface().addImmediateMessage("Received " + item_name + " from " + player_name, "")
            if 100 <= item["item_id"] <= 200: # it is a unit
                grantUnit(item_name)
                CyInterface().addImmediateMessage("Received " + item_name + " from " + player_name, "")
            if 1000 < item["item_id"] <= 1100: # it is gold
                grantGold(item_name)
                CyInterface().addImmediateMessage("Received " + item_name + " from " + player_name, "")
            ArchipelagoData.archipelagoReceivedItems[item_index] = item_name
            ArchipelagoData.saveData()
    else:
        ArchipelagoStuff.showPopup("Connection Error", "Unexpected packet type: " + dataDict.get("cmd"))

def grantTech(techName):
    iPlayerId = gc.getGame().getActivePlayer()
    pPlayer = gc.getPlayer(iPlayerId)
    
    if pPlayer is None or pPlayer.isNone() or not pPlayer.isAlive():
        CyInterface().addImmediateMessage("Player does not exist yet for some reason", "")
        return
    iTeamID = pPlayer.getTeam()
    pTeam = gc.getTeam(iTeamID)
    eTech = gc.getInfoTypeForString(TECH_TRANSLATION_DICT.get(techName))
    # TODO decide what to do about world firsts (fourth parameter)
    pTeam.setHasTech(eTech, True, 0, True, BugOptions.getOption("Archipelago__ShowAnnouncements").getValue())

def grantUnit(itemName):
    iPlayer = gc.getGame().getActivePlayer()
    pPlayer = gc.getPlayer(iPlayer)
    
    if pPlayer is None or pPlayer.isNone():
        return
        
    # Always drop the unit into the Capital city for consistency
    pCapital = pPlayer.getCapitalCity()
    if pCapital is None or pCapital.isNone():
        return
        
    szUnitClass = UNIT_TRANSLATION_DICT.get(itemName)
    if not szUnitClass:
        return
        
    eUnitClass = gc.getInfoTypeForString(szUnitClass)
    if eUnitClass == -1:
        return
        
    # Look up the actual unique Unit Type tied to this player's Civilization
    # (This ensures variants like unique graphics or replacements spawn correctly)
    eUnitType = gc.getCivilizationInfo(pPlayer.getCivilizationType()).getCivilizationUnits(eUnitClass)
    
    if eUnitType != -1:
        # --- THE CANONICAL SPAWN METHOD ---
        # Arguments: (UnitType, bIncrementThreshold, bIncrementExperience)
        pCapital.createGreatPeople(eUnitType, False, False)
        
        # Display an alert notification on the player's main screen
        szUnitName = gc.getUnitInfo(eUnitType).getDescription()
        CyInterface().addImmediateMessage("A unit was born in your capital: " + szUnitName, "")


def grantGold(itemName):
    iPlayerId = gc.getGame().getActivePlayer()
    pPlayer = gc.getPlayer(iPlayerId)
    if pPlayer is None or pPlayer.isNone() or not pPlayer.isAlive():
        CyInterface().addImmediateMessage("Player does not exist yet for some reason", "")
        return 

    try:
        goldAmount = GOLD_TRANSLATION_DICT[itemName]
        # Grant the gold directly into the player's active treasury!
        pPlayer.changeGold(goldAmount)
        
    except Exception, e:
        CyInterface().addImmediateMessage("AP Error granting gold: " + str(e), "")

