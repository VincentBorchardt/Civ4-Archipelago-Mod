from CvPythonExtensions import *
import CvUtil
from PyHelpers import *
from Popup import PyPopup

import BugOptions
#import BugData

import ArchipelagoStuff
import ArchipelagoData
import ArchipelagoEvents
import ArchipelagoConstants

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
            ArchipelagoStuff.showPopup("Received an item", str(item))
            if ArchipelagoData.archipelagoReceivedItems.get(item_index) == item_name:
                continue  # already received item
            if 0 < item["item_id"] <= 100: # it is a tech
                grantTech(item_name)
                CyInterface().addImmediateMessage("Received " + item_name + " from " + player_name, "")
            ArchipelagoData.archipelagoReceivedItems[item_index] = item_name
            ArchipelagoData.saveData()
    else:
        ArchipelagoStuff.showPopup("Connection Error", "Unexpected packet type: " + dataDict.get("cmd"))

def grantTech(item_name):
    """Translates the incoming server item name and safely updates the team state."""
    iPlayerId = gc.getGame().getActivePlayer()
    pPlayer = gc.getPlayer(iPlayerId)
    pTeam = gc.getTeam(pPlayer.getTeam())

    internalTechName = ArchipelagoConstants.TECH_TRANSLATION_DICT[item_name]
    
    # Convert your Archipelago item name string into the engine's internal integer token ID
    # Example: If item_name is "TECH_AGRICULTURE"
    eTech = gc.getInfoTypeForString(internalTechName)
    
    if eTech == -1:
        return
        
    # Trigger loop protection so our event manager knows this is a server reward, NOT human research
    ArchipelagoEvents.bIsReceivingNetworkItem = True
    
    # Grant the tech permanently to the human team
    pTeam.setHasTech(eTech, True, iPlayerId, True, True)
    
    # Restore intercept monitoring
    ArchipelagoEvents.bIsReceivingNetworkItem = False
