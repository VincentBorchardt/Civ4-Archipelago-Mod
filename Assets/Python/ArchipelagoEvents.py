from CvPythonExtensions import *
import CvUtil

import ArchipelagoStuff
import ArchipelagoLocations
import ArchipelagoItems

gc = CyGlobalContext()

def onTechAcquired(argsList):
    """
    Fires whenever any player's team acquires a new technology.
    """
    # Unpack the standard Civ 4 argument list for this event
    eTech, iTeam, iPlayer, bFirst = argsList
    
    # 1. We only care about the human player (usually ID 0)
    # Alternatively, check: if gc.getPlayer(iPlayer).isHuman():
    if gc.getPlayer(iPlayer).isHuman():
        return

    ArchipelagoLocations.checkIfArchipelagoTech(eTech)
    if not ArchipelagoStuff.is_connected_to_ap:
        ArchipelagoStuff.forceSetupPopup()

def onGameStart(argsList):
    """
    Fires once when a brand-new game is initiated (not triggered on loads).
    """
    ArchipelagoItems.loadArchipelagoData()
    ArchipelagoStuff.initialConnectToArchipelago()
    

def onLoadGame(argsList):
    """Fires every time an existing save file is loaded into memory."""
    # 1. First, make sure the dictionary data is loaded from the save
    ArchipelagoItems.loadArchipelagoData()
    ArchipelagoStuff.initialConnectToArchipelago()

    # TODO Change this into a message log once I get that sorted
    ArchipelagoStuff.showPopup()


def onEndPlayerTurn(argsList):
    """
    Fires at the absolute end of an individual player's turn phase.
    """
    iGameTurn, iPlayer = argsList
    
    # We only want to process incoming server checks at the end of the human's turn
    # This prevents the network loop from running on every single AI turn slice
    if gc.getPlayer(iPlayer).isHuman():
        # Trigger your processing loop to fetch new network packets
        ArchipelagoItems.receiveItems()


def onPopupResult(argsList):
    iPopupID, iButtonID, pCustomData = argsList
    
    if iPopupID == 1111:
        # Wrap the result into PyPopup's dedicated return handler
        popupReturn = CyPopupReturn(pCustomData)
        
        # Read the text strings directly from our index slots (0, 1, 2)
        server = popupReturn.getEditBoxString(0)
        username = popupReturn.getEditBoxString(1)
        password = popupReturn.getEditBoxString(2)
        
        # Update your BUG options on the fly
        BugOptions.getOption("Archipelago__ArchipelagoServer").setValue(server)
        BugOptions.getOption("Archipelago__ArchipelagoUsername").setValue(username)
        BugOptions.getOption("Archipelago__ArchipelagoPassword").setValue(password)
        
        # Trigger your connection routine
        ArchipelagoItems.sendAndReceiveData(server, username, password)
                    
