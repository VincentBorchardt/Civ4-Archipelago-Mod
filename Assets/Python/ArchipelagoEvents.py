from CvPythonExtensions import *

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

def onGameStart(argsList):
    """
    Fires once when a brand-new game is initiated (not triggered on loads).
    """
    ArchipelagoItems.loadArchipelagoData()
    
    # TODO Change this into a message log once I get that sorted
    ArchipelagoStuff.showPopup()

def onLoadGame(argsList):
    """Fires every time an existing save file is loaded into memory."""
    # 1. First, make sure the dictionary data is loaded from the save
    ArchipelagoItems.loadArchipelagoData()

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
                    
