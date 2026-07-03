from CvPythonExtensions import *
import CvUtil

import WidgetUtil

import ArchipelagoStuff
import ArchipelagoLocations
import ArchipelagoItems
import ArchipelagoData

gc = CyGlobalContext()
localizer = CyTranslator()

AP_WIDGET_TYPE = None

def initArchipelagoWidgets():
    global AP_WIDGET_TYPE
    
    # 1. Inject a new, unique WidgetType string into the global engine enum pool.
    # This automatically registers it safely inside the engine's memory stack.
    AP_WIDGET_TYPE = WidgetUtil.createWidget("WIDGET_ARCHIPELAGO_GP_CHECK")
    
    # 2. Bind the new engine enum object straight to your custom tooltip callback handler.
    # Note: 'widget=AP_WIDGET_TYPE' explicitly names the keyword argument expected by BUG.
    WidgetUtil.setWidgetHelpFunction(widget=AP_WIDGET_TYPE, func=getArchipelagoButtonHover)

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
    initArchipelagoWidgets()
    ArchipelagoData.loadData()
    ArchipelagoStuff.initialConnectToArchipelago()
    

def onLoadGame(argsList):
    """Fires every time an existing save file is loaded into memory."""
    initArchipelagoWidgets()
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

def onModNetMessage(argsList):
    iMessageId, iData1, iData2, iData3, iData4 = argsList
    
    if iMessageId != 9999: # Match our custom message ID
        return

    iPlayerId = iData1 # Player ID
    iUnitId = iData2   # Unit ID
    
    pPlayer = gc.getPlayer(iPlayerId)
    pUnit = pPlayer.getUnit(iUnitId)
    
    if pUnit and not pUnit.isNone():
        # Now run your logic safely!
        # Because we already validated in handleInput, this is guaranteed safe to commit.
        ArchipelagoLocations.executeGPArchipelagoBulb(pUnit)


def getArchipelagoButtonHover(eWidgetType, iData1, iData2, bOption):
    """
    BUG Callback handler. Returns the dynamic string shown to the player 
    when hovering over the Archipelago action icon.
    """
    # iData1 now carries the Unique Unit Object ID passed from appendMultiListButton
    pUnit = gc.getPlayer(gc.getGame().getActivePlayer()).getUnit(iData1)
    
    # Safely fallback to a general message if the unit evaluation slice drops
    szUnitName = "Great Person"
    if pUnit and not pUnit.isNone():
        szUnitName = gc.getUnitInfo(pUnit.getUnitType()).getDescription()

    return localizer.getText("TXT_KEY_ARCHIPELAGO_GP_HOVER", (szUnitName,))
