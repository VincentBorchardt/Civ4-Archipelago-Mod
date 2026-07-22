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
            if 1000 < item["item_id"] <= 1100: # it is gold
                grantGold(item_name)
                CyInterface().addImmediateMessage("Received " + item_name + " from " + player_name, "")
            ArchipelagoData.archipelagoReceivedItems[item_index] = item_name
            ArchipelagoData.saveData()
    else:
        ArchipelagoStuff.showPopup("Connection Error", "Unexpected packet type: " + dataDict.get("cmd"))

def grantTech(techName):
    # Dynamically grab the active human player ID instead of hardcoding 0
    iPlayerId = gc.getGame().getActivePlayer()
    pPlayer = gc.getPlayer(iPlayerId)
    
    if pPlayer is None or pPlayer.isNone() or not pPlayer.isAlive():
        CyInterface().addImmediateMessage("Player does not exist yet for some reason", "")
        return # Exit early if the player array isn't populated or active
    iTeamID = pPlayer.getTeam()
    pTeam = gc.getTeam(iTeamID)
    eTech = gc.getInfoTypeForString(TECH_TRANSLATION_DICT.get(techName))
    # TODO decide what to do about world firsts (fourth parameter)
    pTeam.setHasTech(eTech, True, 0, True, BugOptions.getOption("Archipelago__ShowAnnouncements").getValue())

def grantGold(item_name):
    # Dynamically grab the active human player ID instead of hardcoding 0
    iPlayerId = gc.getGame().getActivePlayer()
    pPlayer = gc.getPlayer(iPlayerId)
    if pPlayer is None or pPlayer.isNone() or not pPlayer.isAlive():
        CyInterface().addImmediateMessage("Player does not exist yet for some reason", "")
        return 

    try:
        goldAmount = GOLD_TRANSLATION_DICT[item_name]
        # Grant the gold directly into the player's active treasury!
        pPlayer.changeGold(goldAmount)
        
    except Exception, e:
        CyInterface().addImmediateMessage("AP Error granting gold: " + str(e), "")

