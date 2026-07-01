from CvPythonExtensions import *
import CvUtil

import ArchipelagoStuff
import ArchipelagoLocations
import ArchipelagoItems
import ArchipelagoData

gc = CyGlobalContext()

# Arbitrary unique interface ID for our custom button
AP_GP_BUTTON_ID = "ArchipelagoGPCheckButton"
# Custom network message macro identifier
AP_NET_MESSAGE_ID = 9999 

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
    ArchipelagoData.loadData()
    ArchipelagoStuff.initialConnectToArchipelago()
    

def onLoadGame(argsList):
    """Fires every time an existing save file is loaded into memory."""
    ArchipelagoData.loadData()
    ArchipelagoStuff.initialConnectToArchipelago()


def onEndPlayerTurn(argsList):
    """
    Fires at the absolute end of an individual player's turn phase.
    """
    iGameTurn, iPlayer = argsList
    # We only want to process incoming server checks at the end of the human's turn
    # This prevents the network loop from running on every single AI turn slice
    if gc.getPlayer(iPlayer).isHuman():
        if not ArchipelagoData.hasConnectedToArchipelago:
            ArchipelagoStuff.showPopup("Set Up Archipelago Connection Settings", "Go into the BUG Options (Alt+Ctrl+O) and enter in your connection information.")
        else:
            # Trigger your processing loop to fetch new network packets
            ArchipelagoItems.receiveItems()
            if not ArchipelagoData.isConnectedToArchipelago:
                ArchipelagoStuff.showPopup("Archipelago Connection Lost", "Check your settings and make sure the client is open and the server is up.")

def updateArchipelagoGPButton(screen, pHeadSelectedUnit):
    """
    Called directly from CvMainInterface.py inside the selection button
    draw cycle to add the Archipelago check button.
    """
    # Ensure player is connected to the server
    if not ArchipelagoData.isConnectedToArchipelago:
        return

    # Check if the unit is a valid Great Person type
    info = gc.getUnitInfo(pHeadSelectedUnit.getUnitType())
    szClassType = gc.getUnitClassInfo(info.getUnitClassType()).getType()
    
    validGPs = [
        "UNITCLASS_SCIENTIST", 
        "UNITCLASS_ENGINEER", 
        "UNITCLASS_PROPHET", 
        "UNITCLASS_ARTIST", 
        "UNITCLASS_MERCHANT", 
        "UNITCLASS_GREAT_GENERAL",
        "UNITCLASS_GREAT_SPY",
    ]
    
    if szClassType in validGPs:
        # Places the standard text button nicely above the action tray array.
        # Coordinates (X: 210, Y: 110) prevent collisions with basic multi-unit trays.
        screen.setButtonGFC(AP_GP_BUTTON_ID, "Send GP Check", "", 210, 110, 150, 30, 
                            WidgetTypes.WIDGET_GENERAL, AP_NET_MESSAGE_ID, pHeadSelectedUnit.getID(), 
                            ButtonStyles.BUTTON_STYLE_STANDARD)
        screen.show(AP_GP_BUTTON_ID)
