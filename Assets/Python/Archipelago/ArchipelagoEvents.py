from CvPythonExtensions import *
import CvUtil

import WidgetUtil

import ArchipelagoStuff
import ArchipelagoLocations
import ArchipelagoItems
import ArchipelagoData
import ArchipelagoConstants

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
    CyInterface().addImmediateMessage("In onTechAcquired", "")
    # Unpack the standard Civ 4 argument list for this event
    eTech, iTeam, iPlayer, bFirst = argsList
    
    # 1. We only care about the human player (usually ID 0)
    # Alternatively, check: if gc.getPlayer(iPlayer).isHuman():
    if not gc.getPlayer(iPlayer).isHuman():
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

def onBuildingBuilt(argsList):
    """
    Fires the exact frame a building finishes construction inside any city.
    """
    # Arguments passed by the engine: (pCity, eBuildingType)
    pCity, eBuilding = argsList
    if not ArchipelagoData.archipelagoWorldWondersanityEnabled:
        return
    if pCity is None or pCity.isNone():
        return    
    iPlayerId = pCity.getOwner()
    pPlayer = gc.getPlayer(iPlayerId)
    
    # 1. Only process completion locations driven by the human player
    if not pPlayer.isHuman():
        return  
    buildingInfo = gc.getBuildingInfo(eBuilding)
    buildingClassInfo = gc.getBuildingClassInfo(buildingInfo.getBuildingClassType())
    
    # 2. Check if the completed building is classified as a unique World Wonder
    if buildingClassInfo.getMaxGlobalInstances() == 1:
        
        if buildingInfo.getGlobalReligionCommerce() > 0 or buildingInfo.getGlobalCorporationCommerce() > 0:
            return # Safely ignore holy shrines and corporate headquarters!
        szBuildingType = buildingInfo.getType() # e.g., "BUILDING_STONEHENGE"
        
        # 3. Route to your serialization engine to map the location check
        CyInterface().addImmediateMessage("Wonder Location Sent! Type: " + szBuildingType, "")
        ArchipelagoLocations.sendLocationCheck(szBuildingType)


def onVictory(argsList):
    """Fires the exact frame a victory condition is achieved on the map."""
    iWinningTeam, eVictoryType = argsList
    
    # 1. Check if the active human player is part of the winning team
    iActivePlayer = gc.getGame().getActivePlayer()
    pPlayer = gc.getPlayer(iActivePlayer)
    
    if pPlayer.getTeam() == iWinningTeam:
        # 2. Extract the canonical XML Type string of the victory (e.g., "VICTORY_SPACE_RACE")
        szVictoryTypeStr = gc.getVictoryInfo(eVictoryType).getType()
        victoryLocation = ArchipelagoConstants.VICTORY_TRANSLATION_DICT.get(szVictoryTypeStr)
        if victoryLocation:
            messageDict = {"type": "Victory", "victoryType": victoryLocation}
            ArchipelagoStuff.sendAndReceiveData(messageDict, waitForRead=False)
            CyInterface().addImmediateMessage("Archipelago Victory Condition Sent! Type: " + victoryLocation, "")


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
