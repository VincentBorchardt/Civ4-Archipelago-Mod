from CvPythonExtensions import *
import CvUtil
from PyHelpers import *
from Popup import PyPopup

import BugOptions

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

# TODO Figure out a way to save this so you don't receive duplicates
archipelagoReceivedItems = {}

def receiveItems():
    messageDict = {"type":"ReceiveItems"}
    dataDict = ArchipelagoStuff.sendAndReceiveData(messageDict, waitForRead=True)
    CyInterface().addImmediateMessage(str(dataDict), "")
    CyInterface().addImmediateMessage(dataDict.get("cmd"), "")
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
    else:
        ArchipelagoStuff.showPopup("Connection Error", "Unexpected packet type: " + dataDict.get("cmd"))

def grantTech(techName):
    CyInterface().addImmediateMessage(techName, "")
    CyInterface().addImmediateMessage(TECH_TRANSLATION_DICT.get(techName), "")
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
