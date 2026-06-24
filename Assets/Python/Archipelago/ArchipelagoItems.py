from CvPythonExtensions import *
import CvUtil
from PyHelpers import *
from Popup import PyPopup

import BugOptions
import BugData

import ArchipelagoStuff

import math

# constants
gc = CyGlobalContext()
cyGame = CyGame()
cyMap = CyMap()
pyGame = PyGame()

TECH_TRANSLATION_DICT = {
    "Agriculture" : "TECH_AGRICULTURE"
}

AP_DATA_KEY = "ArchipelagoMod"

archipelagoReceivedItems = {}

def saveArchipelagoData(*args):
    """Saves the tracking dictionary into BUG's secure data registry."""
    global archipelagoReceivedItems
    try:
        # Get the global BUG data registry
        data = BugData.getGameData()
        # Store your dictionary inside your unique namespace slot
        data[AP_DATA_KEY] = archipelagoReceivedItems
    except Exception, e:
        CyInterface().addImmediateMessage("AP Save Error: " + str(e), "")

def loadArchipelagoData(*args):
    """Loads the tracking dictionary from BUG's data registry."""
    global archipelagoReceivedItems
    try:
        data = BugData.getGameData()
        # Retrieve your dictionary, defaulting to an empty dict if it doesn't exist yet
        if AP_DATA_KEY in data:
            archipelagoReceivedItems = data[AP_DATA_KEY]
        else:
            archipelagoReceivedItems = {}
    except Exception, e:
        CyInterface().addImmediateMessage("AP Load Error: " + str(e), "")
        archipelagoReceivedItems = {}


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
            if archipelagoReceivedItems.get(item_index) == item_name:
                continue  # already received item
            if 0 < item["item_id"] < 1000: # it is a tech
                grantTech(item_name)
                CyInterface().addImmediateMessage("Received " + item_name + " from " + player_name, "")
            archipelagoReceivedItems[item_index] = item_name
            saveArchipelagoData()
    else:
        ArchipelagoStuff.showPopup("Connection Error", "Unexpected packet type: " + dataDict.get("cmd"))

def grantTech(techName):
    pPlayer = gc.getPlayer(0)
    if pPlayer is None or pPlayer.isNone() or not pPlayer.isAlive():
        CyInterface().addImmediateMessage("Player does not exist yet for some reason", "")
        return # Exit early if the player array isn't populated or active
    iTeamID = pPlayer.getTeam()
    pTeam = gc.getTeam(iTeamID)
    eTech = gc.getInfoTypeForString(TECH_TRANSLATION_DICT.get(techName))
    # TODO decide what to do about world firsts (fourth parameter)
    # TODO make a setting for showing tech announcements
    pTeam.setHasTech(eTech, True, 0, True, False)
