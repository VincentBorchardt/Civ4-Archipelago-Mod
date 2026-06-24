## ArchipelagoData.py
## Centralized persistence and cross-module state tracking cache

from CvPythonExtensions import *
import BugData

# Unique storage tracking slot inside BUG's secure save profile
DATA_SAVE_KEY = "ArchipelagoModSaveState"

# Cross-module active memory cache state objects
hasConnectedToArchipelago = False
isConnectedToArchipelago = False
archipelagoReceivedItems = {}

def saveData():
    """Serializes the multiworld data arrays straight into BUG's safe profile registry."""
    try:
        dataStore = BugData.getGameData()
        
        # Consolidate all parameters into a single master dictionary payload
        payload = {
            "hasConnected": hasConnectedToArchipelago,
            "receivedItems": archipelagoReceivedItems
        }
        
        dataStore[DATA_SAVE_KEY] = payload
    except Exception, e:
        CyInterface().addImmediateMessage("AP Save Data Failure: " + str(e), "")

def loadData(*args):
    """Deserializes arrays out of BUG's secure profile registry on boot loops."""
    global hasConnectedToArchipelago, archipelagoReceivedItems
    try:
        dataStore = BugData.getGameData()
        
        if DATA_SAVE_KEY in dataStore:
            payload = dataStore[DATA_SAVE_KEY]
            
            # Extract attributes safely
            hasConnectedToArchipelago = payload.get("hasConnected", False)
            archipelagoReceivedItems = payload.get("receivedItems", {})
        else:
            hasConnectedToArchipelago = False
            archipelagoReceivedItems = {}
            
    except Exception, e:
        CyInterface().addImmediateMessage("AP Load Data Failure: " + str(e), "")
        hasConnectedToArchipelago = False
        archipelagoReceivedItems = {}
