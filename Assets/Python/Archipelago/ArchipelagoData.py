## ArchipelagoData.py
## Centralized persistence and cross-module state tracking cache

from CvPythonExtensions import *
import BugData
import BugOptions

import ArchipelagoStuff

# Unique storage tracking slot inside BUG's secure save profile
DATA_SAVE_KEY = "ArchipelagoModSaveState"

# TODO decapitalize 'sanity' once I have good refactoring tools
hasConnectedToArchipelago = False
isConnectedToArchipelago = False
archipelagoCheckedLocations = []
archipelagoReceivedItems = {}
archipelagoGPChecks = {}
archipelagoMaxGPSanity = 0
archipelagoTechsanityEnabled = False
archipelagoWorldWondersanityEnabled = False
archipelagoNationalWondersanityEnabled = False # TODO make this false once I add in the setting
archipelagoHints = []


def saveData():
    """Serializes trackers and instance connection settings straight into the save game."""
    try:
        dataStore = BugData.getGameData()
        
        # 1. Fetch current settings active in BUG options memory
        server = BugOptions.getOption("Archipelago__ArchipelagoServer").getValue()
        username = BugOptions.getOption("Archipelago__ArchipelagoUsername").getValue()
        password = BugOptions.getOption("Archipelago__ArchipelagoPassword").getValue()
        
        # 2. Package everything together into our save state dictionary payload
        payload = {
            "hasConnected": hasConnectedToArchipelago,
            "checkedLocations": archipelagoCheckedLocations,
            "receivedItems": archipelagoReceivedItems,
            "receivedHints": archipelagoHints,
            "savedServer": server,
            "savedUser": username,
            "savedPass": password,
            "gpChecks": archipelagoGPChecks,
            "maxGPsanity": archipelagoMaxGPSanity,
            "techsanity": archipelagoTechsanityEnabled,
            "worldWondersanity": archipelagoWorldWondersanityEnabled,
            "nationalWondersanity": archipelagoNationalWondersanityEnabled,
            
        }
        
        dataStore[DATA_SAVE_KEY] = payload
    except Exception, e:
        CyInterface().addImmediateMessage("AP Save Data Failure: " + str(e), "")

def loadData(*args):
    """Deserializes arrays out of the save, falling back to universal INI settings if missing."""
    global hasConnectedToArchipelago, archipelagoCheckedLocations, archipelagoReceivedItems, archipelagoHints, archipelagoGPChecks, archipelagoMaxGPSanity, archipelagoTechsanityEnabled, archipelagoWorldWondersanityEnabled, archipelagoNationalWondersanityEnabled
    isConnectedToArchipelago = False
    try:
        dataStore = BugData.getGameData()
        
        if DATA_SAVE_KEY in dataStore:
            payload = dataStore[DATA_SAVE_KEY]
            
            # Extract standard tracking parameters safely
            hasConnectedToArchipelago = payload.get("hasConnected", False)
            archipelagoCheckedLocations = payload.get("checkedLocations", [])
            archipelagoReceivedItems = payload.get("receivedItems", {})
            archipelagoHints = payload.get("receivedHints", [])
            archipelagoGPChecks = payload.get("gpChecks", {})
            archipelagoMaxGPSanity = payload.get("maxGPsanity", 0)
            archipelagoTechsanityEnabled = payload.get("techsanity", False)
            archipelagoWorldWondersanityEnabled = payload.get("worldWondersanity", False)
            archipelagoNationalWondersanityEnabled = payload.get("nationalWondersanity", False)
            
            # 3. DUAL-LAYER FALLBACK LOGIC: Check for save-specific connection data
            saved_server = payload.get("savedServer", None)
            saved_user = payload.get("savedUser", None)
            saved_pass = payload.get("savedPass", None)
            
            # If the data exists in this specific save file, overwrite active BUG options
            if saved_server is not None and saved_user is not None and saved_pass is not None:
                BugOptions.getOption("Archipelago__ArchipelagoServer").setValue(saved_server)
                BugOptions.getOption("Archipelago__ArchipelagoUsername").setValue(saved_user)
                BugOptions.getOption("Archipelago__ArchipelagoPassword").setValue(saved_pass)
        else:
            # TODO extract this list of settings
            hasConnectedToArchipelago = False
            archipelagoCheckedLocations = []
            archipelagoReceivedItems = {}
            archipelagoHints = []
            archipelagoGPChecks = {}
            archipelagoMaxGPSanity = 0
            archipelagoTechsanityEnabled = False
            archipelagoWorldWondersanityEnabled = False
            archipelagoNationalWondersanityEnabled = False
            
    except Exception, e:
        CyInterface().addImmediateMessage("AP Load Data Failure: " + str(e), "")
        hasConnectedToArchipelago = False
        archipelagoCheckedLocations = []
        archipelagoReceivedItems = {}
        archipelagoHints = []
        archipelagoGPChecks = {}
        archipelagoMaxGPSanity = 0
        archipelagoTechsanityEnabled = False
        archipelagoWorldWondersanityEnabled = False
        archipelagoNationalWondersanityEnabled = False

##def getSettings():
##    global archipelagoSettings
##    messageDict = {"type":"GetSettings"}
##    dataDict = ArchipelagoStuff.sendAndReceiveData(messageDict)
##    if not dataDict or (dataDict.get("cmd") != "GetSettings"):
##        ArchipelagoStuff.showPopup("Connection Error", "No settings packet received")
##        return
##    #TODO set up settings!
##    saveData()

def setSettings(dataDict):
    global archipelagoMaxGPSanity, archipelagoTechsanityEnabled, archipelagoWorldWondersanityEnabled, archipelagoNationalWondersanityEnabled
    CyInterface().addImmediateMessage(str(dataDict), "")
    archipelagoMaxGPSanity = dataDict["gpsanity"]
    if dataDict["techsanity"] > 0:
        archipelagoTechsanityEnabled = True
    if dataDict["worldWondersanity"] > 0:
        archipelagoWorldWondersanityEnabled = True
    if dataDict["nationalWondersanity"] > 0:
        archipelagoNationalWondersanityEnabled = True
    saveData()

def getHints():
    global archipelagoHints
    messageDict = {"type":"GetHints"}
    dataDict = ArchipelagoStuff.sendAndReceiveData(messageDict)
    if not dataDict or (dataDict.get("cmd") != "GetHints"):
        ArchipelagoStuff.showPopup("Connection Error", "No hint packet received")
        return
    archipelagoHints = dataDict.get("hints")
    saveData()
