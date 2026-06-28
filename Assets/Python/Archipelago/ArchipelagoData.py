## ArchipelagoData.py
## Centralized persistence and cross-module state tracking cache

from CvPythonExtensions import *
import BugData
import BugOptions

import ArchipelagoStuff

# Unique storage tracking slot inside BUG's secure save profile
DATA_SAVE_KEY = "ArchipelagoModSaveState"

# Cross-module active memory cache state objects
hasConnectedToArchipelago = False
isConnectedToArchipelago = False
archipelagoReceivedItems = {}
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
            "receivedItems": archipelagoReceivedItems,
            "receivedHints": archipelagoHints,
            "savedServer": server,
            "savedUser": username,
            "savedPass": password
        }
        
        dataStore[DATA_SAVE_KEY] = payload
    except Exception, e:
        CyInterface().addImmediateMessage("AP Save Data Failure: " + str(e), "")

def loadData(*args):
    """Deserializes arrays out of the save, falling back to universal INI settings if missing."""
    global hasConnectedToArchipelago, archipelagoReceivedItems, archipelagoHints
    try:
        dataStore = BugData.getGameData()
        
        if DATA_SAVE_KEY in dataStore:
            payload = dataStore[DATA_SAVE_KEY]
            
            # Extract standard tracking parameters safely
            hasConnectedToArchipelago = payload.get("hasConnected", False)
            archipelagoReceivedItems = payload.get("receivedItems", {})
            archipelagoHints = payload.get("receivedHints", [])
            
            # 3. DUAL-LAYER FALLBACK LOGIC: Check for save-specific connection data
            saved_server = payload.get("savedServer", None)
            saved_user = payload.get("savedUser", None)
            saved_pass = payload.get("savedPass", None)
            
            # If the data exists in this specific save file, overwrite active BUG options
            if saved_server is not None and saved_user is not None and saved_pass is not None:
                BugOptions.getOption("Archipelago__ArchipelagoServer").setValue(saved_server)
                BugOptions.getOption("Archipelago__ArchipelagoUsername").setValue(saved_user)
                BugOptions.getOption("Archipelago__ArchipelagoPassword").setValue(saved_pass)
                # Note: If these keys are None (e.g. an old save file generated before this update),
                # Python skips this block entirely, cleanly falling back to whatever is inside the .ini file!
        else:
            # Baseline defaults for a completely brand-new game map
            hasConnectedToArchipelago = False
            archipelagoReceivedItems = {}
            archipelagoHints = []
            
    except Exception, e:
        CyInterface().addImmediateMessage("AP Load Data Failure: " + str(e), "")
        hasConnectedToArchipelago = False
        archipelagoReceivedItems = {}
        archipelagoHints = []

def getHints():
    global archipelagoHints
    messageDict = {"type":"GetHints"}
    dataDict = ArchipelagoStuff.sendAndReceiveData(messageDict)
    if not dataDict or (dataDict.get("cmd") != "GetHints"):
        ArchipelagoStuff.showPopup("Connection Error", "No hint packet received")
        return
    archipelagoHints = dataDict.get("hints")
    saveData()
