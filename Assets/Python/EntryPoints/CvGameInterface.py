## Sid Meier's Civilization 4
## Copyright Firaxis Games 2005
##
## #####   WARNING - MODIFYING THE FUNCTION NAMES OF THIS FILE IS PROHIBITED  #####
## 
## The app specifically calls the functions as they are named. Use this file to pass 
## args to another file that contains your modifications
##
## MODDERS - If you create a GameUtils file, update the CvGameInterfaceFile reference to point to your new file

#
import CvUtil
import CvGameUtils
import CvGameInterfaceFile
import CvEventInterface
from CvPythonExtensions import *

# globals
gc = CyGlobalContext()
normalGameUtils = CvGameInterfaceFile.GameUtils

def gameUtils():
    ' replace normalGameUtils with your mod version'
    return normalGameUtils

def isVictoryTest():
    #CvUtil.pyPrint( "CvGameInterface.isVictoryTest" )
    return gameUtils().isVictoryTest()

def isVictory(argsList):
    return gameUtils().isVictory(argsList)

def isPlayerResearch(argsList):
    #CvUtil.pyPrint( "CvGameInterface.isPlayerResearch" )
    return gameUtils().isPlayerResearch(argsList)

def getExtraCost(argsList):
    #CvUtil.pyPrint( "CvGameInterface.getExtraCost" )
    return gameUtils().getExtraCost(argsList)

def createBarbarianCities():
    #CvUtil.pyPrint( "CvGameInterface.createBarbarianCities" )
    return gameUtils().createBarbarianCities()

def createBarbarianUnits():
    #CvUtil.pyPrint( "CvGameInterface.createBarbarianUnits" )
    return gameUtils().createBarbarianUnits()

def skipResearchPopup(argsList):
    #CvUtil.pyPrint( "CvGameInterface.skipResearchPopup" )
    return gameUtils().skipResearchPopup(argsList)

def showTechChooserButton(argsList):
    #CvUtil.pyPrint( "CvGameInterface.showTechChooserButton" )
    return gameUtils().showTechChooserButton(argsList)

def getFirstRecommendedTech(argsList):
    #CvUtil.pyPrint( "CvGameInterface.getFirstRecommendedTech" )
    return gameUtils().getFirstRecommendedTech(argsList)

def getSecondRecommendedTech(argsList):
    #CvUtil.pyPrint( "CvGameInterface.getSecondRecommendedTech" )
    return gameUtils().getSecondRecommendedTech(argsList)

def skipProductionPopup(argsList):
    #CvUtil.pyPrint( "CvGameInterface.skipProductionPopup" )
    return gameUtils().skipProductionPopup(argsList)

def canRazeCity(argsList):
    #CvUtil.pyPrint( "CvGameInterface.canRazeCity" )
    return gameUtils().canRazeCity(argsList)

def canDeclareWar(argsList):
    #CvUtil.pyPrint( "CvGameInterface.canRazeCity" )
    return gameUtils().canDeclareWar(argsList)

def showExamineCityButton(argsList):
    #CvUtil.pyPrint( "CvGameInterface.showExamineCityButton" )
    return gameUtils().showExamineCityButton(argsList)

def getRecommendedUnit(argsList):
    #CvUtil.pyPrint( "CvGameInterface.getRecommendedUnit" )
    return gameUtils().getRecommendedUnit(argsList)

def getRecommendedBuilding(argsList):
    #CvUtil.pyPrint( "CvGameInterface.getRecommendedBuilding" )
    return gameUtils().getRecommendedBuilding(argsList)

def updateColoredPlots():
    #CvUtil.pyPrint( "CvGameInterface.updateColoredPlots" )
    return gameUtils().updateColoredPlots()

def isActionRecommended(argsList):
    #CvUtil.pyPrint( "CvGameInterface.isActionRecommended" )
    return gameUtils().isActionRecommended(argsList)

def unitCannotMoveInto(argsList):
    return gameUtils().unitCannotMoveInto(argsList)

def cannotHandleAction(argsList):
    iAction, iCommand, iData = argsList
    
    # 1. Pull the structural Action Info block out of the global cache
    actionInfo = gc.getActionInfo(iCommand)
    
    # 2. Check if this specific action triggers the C++ bulb mission (MISSION_DISCOVER)
    if actionInfo.getMissionType() == MissionTypes.MISSION_DISCOVER:
        import ArchipelagoData
        
        # 3. Only block the human player if Techsanity is currently active
        if ArchipelagoData.archipelagoTechsanityEnabled:
            iActivePlayer = gc.getGame().getActivePlayer()
            if gc.getPlayer(iActivePlayer).isHuman():
                return True
                
    # 4. Fallback directly to the native GameUtils rule engine guidelines
    return gameUtils().cannotHandleAction(argsList)


def canBuild(argsList):
    #CvUtil.pyPrint( "CvGameInterface.canBuild" )
    return gameUtils().canBuild(argsList)

def cannotFoundCity(argsList):
    #CvUtil.pyPrint( "CvGameInterface.cannotHandleAction" )
    return gameUtils().cannotFoundCity(argsList)

def cannotSelectionListMove(argsList):
    #CvUtil.pyPrint( "CvGameInterface.cannotSelectionListMove" )
    return gameUtils().cannotSelectionListMove(argsList)

def cannotSelectionListGameNetMessage(argsList):
    #CvUtil.pyPrint( "CvGameInterface.cannotSelectionListGameNetMessage" )
    return gameUtils().cannotSelectionListGameNetMessage(argsList)

def cannotDoControl(argsList):
    #CvUtil.pyPrint( "CvGameInterface.cannotDoControl" )
    return gameUtils().cannotDoControl(argsList)

def canResearch(argsList):
    #CvUtil.pyPrint( "CvGameInterface.canResearch" )
    return gameUtils().canResearch(argsList)

def cannotResearch(argsList):
    #CvUtil.pyPrint( "CvGameInterface.cannotResearch" )
    ePlayer, eTech, bTrade = argsList
    
    try:
        import ArchipelagoLocations
        if ArchipelagoLocations.cannotResearchTechsanityGate(ePlayer, eTech):
            return True
    except Exception, e:
        pass

    return gameUtils().cannotResearch(argsList)

def canDoCivic(argsList):
    #CvUtil.pyPrint( "CvGameInterface.canDoCivic" )
    return gameUtils().canDoCivic(argsList)

def cannotDoCivic(argsList):
    #CvUtil.pyPrint( "CvGameInterface.cannotDoCivic" )
    return gameUtils().cannotDoCivic(argsList)

def canTrain(argsList):
    #CvUtil.pyPrint( "CvGameInterface.canTrain" )
    return gameUtils().canTrain(argsList)

def cannotTrain(argsList):
    #CvUtil.pyPrint( "CvGameInterface.cannotTrain" )
    pCity, eUnit, bContinue, bTestVisible, bIgnoreCost, bIgnoreUpgrades = argsList
    if pCity is None or pCity.isNone():
        return gameUtils().cannotTrain(argsList)

    iPlayer = pCity.getOwner()
    pPlayer = gc.getPlayer(iPlayer)
    unitInfo = gc.getUnitInfo(eUnit)
    szUnitType = unitInfo.getType() # e.g., "UNIT_AP_BOWMAN"

    # Target only our custom freestanding Archipelago Unique Units
    if szUnitType.startswith("UNIT_AP_"):
        if not (pPlayer and not pPlayer.isNone() and pPlayer.isHuman()):
            return True

        import ArchipelagoData
        # 1. Hard-hide and block the unique option if the network token hasn't arrived
        if szUnitType not in ArchipelagoData.archipelagoUnlockedUUs:
            return True

    return gameUtils().cannotTrain(argsList)

def canConstruct(argsList):
    # CvUtil.pyPrint( "CvGameInterface.canConstruct" )
    pCity, eBuilding, bContinue, bTestVisible, bIgnoreCost = argsList


    if pCity is None or pCity.isNone():
        return gameUtils().canConstruct(argsList)

    iPlayer = pCity.getOwner()
    pPlayer = gc.getPlayer(iPlayer)

    if pPlayer and not pPlayer.isNone() and pPlayer.isHuman():
        buildingInfo = gc.getBuildingInfo(eBuilding)
        szBuildingType = buildingInfo.getType()
        eObsoleteTech = buildingInfo.getObsoleteTech()
        buildingClassInfo = gc.getBuildingClassInfo(buildingInfo.getBuildingClassType())
        CvUtil.pyPrint("Archipelago Profiler -> Running canConstruct for building: %s" % szBuildingType)

        # === INTERCEPTOR A: WONDER OBSOLESCENCE SPOOFING ===
        # TODO add in a check for wonder obsolescence settings
        # TODO need to fix the case where both interceptors are needed (Great Lighthouse)
        if buildingClassInfo.getMaxGlobalInstances() == 1 and eObsoleteTech != -1:
            CvUtil.pyPrint("Starting Interceptor A")
            pTeam = gc.getTeam(pPlayer.getTeam())
            if pTeam.isHasTech(eObsoleteTech):
                if gc.getGame().getBuildingClassCreatedCount(buildingInfo.getBuildingClassType()) == 0:
                    pTeam.setHasTech(eObsoleteTech, False, iPlayer, False, False)
                    bNativelyBuildableWithoutObsolescence = pCity.canConstruct(eBuilding, bContinue, bTestVisible, bIgnoreCost)
                    pTeam.setHasTech(eObsoleteTech, True, iPlayer, False, False)

                    if bNativelyBuildableWithoutObsolescence:
                        return True
                    else:
                        return False

        # === INTERCEPTOR B: UNIQUE BUILDING PREREQUISITE SPOOFING ===
        if bTestVisible:
            return gameUtils().canConstruct(argsList)
        
        import ArchipelagoConstants
        if szBuildingType in ArchipelagoConstants.BUILDINGS_THAT_NEED_SPOOF_CHECK:
            spoofedLocalBuildings = []
            spoofedGlobalCities = []  # Tracks (pLoopCity, eVanillaBuilding) pairs for cleanup
            apLoopCount = 0
            globalLoopCount = 0

            CvUtil.pyPrint("Starting Interceptor B")

            # Check if the building being evaluated is a National requiring global counts
            targetGlobalPrereqClass = ArchipelagoConstants.NATIONAL_WONDER_PREREQS.get(szBuildingType)

            # Scan through all 34 entries to see if this city contains an unlocked AP replacement
            for ap_type, vanilla_class_str in ArchipelagoConstants.AP_BUILDING_TO_VANILLA_CLASS.iteritems():
                apLoopCount += 1
                eAPBuilding = gc.getInfoTypeForString(ap_type)
                if eAPBuilding != -1:
                    eVanillaClass = gc.getInfoTypeForString(vanilla_class_str)
                    if eVanillaClass != -1:
                        eVanillaBuilding = gc.getCivilizationInfo(pPlayer.getCivilizationType()).getCivilizationBuildings(eVanillaClass)
                        if eVanillaBuilding == -1:
                            continue

                        # CASE 1: Global Prerequisite
                        if targetGlobalPrereqClass and vanilla_class_str == targetGlobalPrereqClass:
                            globalLoopCount += 1
                            # Iterate through EVERY city the player owns to find AP equivalents
                            (pLoopCity, iter) = pPlayer.firstCity(False)
                            while pLoopCity:
                                if not pLoopCity.isNone() and pLoopCity.getNumRealBuilding(eAPBuilding) > 0:
                                    # If this city has an AP building and no vanilla version, spoof!
                                    if pLoopCity.getNumRealBuilding(eVanillaBuilding) == 0:
                                        pLoopCity.setNumRealBuilding(eVanillaBuilding, 1)
                                        spoofedGlobalCities.append((pLoopCity, eVanillaBuilding))
                                (pLoopCity, iter) = pPlayer.nextCity(iter, False)

                        # CASE 2: Standard Local City Prerequisite
                        # TODO should this be elif? I want to make sure the normal prereq is still being followed
                        # AKA you need a University in the city you're building Oxford, even if you have enough
                        elif pCity.getNumRealBuilding(eAPBuilding) > 0:
                            if pCity.getNumRealBuilding(eVanillaBuilding) == 0:
                                pCity.setNumRealBuilding(eVanillaBuilding, 1)
                                spoofedLocalBuildings.append(eVanillaBuilding)

            # Execute standard validation loops while the ghost structures satisfy child prerequisite trees
            if len(spoofedLocalBuildings) > 0 or len(spoofedGlobalCities) > 0:
                bCanConstructNatively = pCity.canConstruct(eBuilding, bContinue, bTestVisible, bIgnoreCost)

                # Instant Clean Up - Local
                for eVanillaBuilding in spoofedLocalBuildings:
                    pCity.setNumRealBuilding(eVanillaBuilding, 0)

                # Instant Clean Up - Global Empire Loop
                for pLoopCity, eVanillaBuilding in spoofedGlobalCities:
                    pLoopCity.setNumRealBuilding(eVanillaBuilding, 0)

                if apLoopCount > 0:
                    CvUtil.pyPrint("AP checking loop " + str(apLoopCount) + " times")

                if globalLoopCount > 0:
                    CvUtil.pyPrint("Global spoofing loop ran " + str(globalLoopCount) + " times")
                    #CyInterface().addImmediateMessage("Spoofing loop ran " + str(globalLoopCount) + " times", "")

                if bCanConstructNatively:
                    return True
                else:
                    return False

    return gameUtils().canConstruct(argsList)


def cannotConstruct(argsList):
    #CvUtil.pyPrint( "CvGameInterface.cannotConstruct" )
    pCity, eBuilding, bContinue, bTestVisible, bIgnoreCost = argsList
    if pCity is None or pCity.isNone():
        return gameUtils().cannotConstruct(argsList)

    iPlayer = pCity.getOwner()
    pPlayer = gc.getPlayer(iPlayer)
    buildingInfo = gc.getBuildingInfo(eBuilding)
    szBuildingType = buildingInfo.getType()

    # Intercept only our custom freestanding Archipelago Unique Buildings
    if szBuildingType.startswith("BUILDING_AP_"):
        # 1. Hard-block the AI from ever seeing or training these items
        if pPlayer is None or pPlayer.isNone() or not pPlayer.isHuman():
            return True

        # 2. Hard-hide the item for the human player if the network item hasn't settled yet
        import ArchipelagoData
        if szBuildingType not in ArchipelagoData.archipelagoUnlockedUBs:
            return True

    return gameUtils().cannotConstruct(argsList)

def canCreate(argsList):
    #CvUtil.pyPrint( "CvGameInterface.canCreate" )
    return gameUtils().canCreate(argsList)

def cannotCreate(argsList):
    #CvUtil.pyPrint( "CvGameInterface.cannotCreate" )
    return gameUtils().cannotCreate(argsList)

def canMaintain(argsList):
    #CvUtil.pyPrint( "CvGameInterface.canMaintain" )
    return gameUtils().canMaintain(argsList)

def cannotMaintain(argsList):
    #CvUtil.pyPrint( "CvGameInterface.cannotMaintain" )
    return gameUtils().cannotMaintain(argsList)

def AI_chooseTech(argsList):
    'AI chooses what to research'
    #CvUtil.pyPrint( "CvGameInterface.AI_chooseTech" )
    return gameUtils().AI_chooseTech(argsList)

def AI_chooseProduction(argsList):
    'AI chooses city production'
    #CvUtil.pyPrint( "CvGameInterface.AI_chooseProduction" )
    return gameUtils().AI_chooseProduction(argsList)

def AI_unitUpdate(argsList):
    'AI moves units - return 0 to let AI handle it, return 1 to say that the move is handled in python '
    #CvUtil.pyPrint( "CvGameInterface.AI_unitUpdate" )
    return gameUtils().AI_unitUpdate(argsList)

def AI_doWar(argsList):
    'AI decides whether to make war or peace - return 0 to let AI handle it, return 1 to say that the move is handled in python '
    #CvUtil.pyPrint( "CvGameInterface.AI_doWar" )
    return gameUtils().AI_doWar(argsList)

def AI_doDiplo(argsList):
    'AI decides does diplomacy for the turn - return 0 to let AI handle it, return 1 to say that the move is handled in python '
    #CvUtil.pyPrint( "CvGameInterface.AI_doDiplo" )
    return gameUtils().AI_doDiplo(argsList)

def calculateScore(argsList):
    return gameUtils().calculateScore(argsList)

def doHolyCity():
    #CvUtil.pyPrint( "CvGameInterface.doHolyCity" )
    return gameUtils().doHolyCity()

def doHolyCityTech(argsList):
    #CvUtil.pyPrint( "CvGameInterface.doHolyCityTech" )
    return gameUtils().doHolyCityTech(argsList)

def doGold(argsList):
    #CvUtil.pyPrint( "CvGameInterface.doGold" )
    return gameUtils().doGold(argsList)

def doResearch(argsList):
    #CvUtil.pyPrint( "CvGameInterface.doResearch" )
    return gameUtils().doResearch(argsList)

def doGoody(argsList):
    # FIX: Correctly unpack the native arguments: GoodyType, CyPlot, CyUnit
    eGoodyType, pPlot, pUnit = argsList
    
    if pUnit is None or pUnit.isNone():
        return gameUtils().doGoody(argsList)
        
    # Extract the owner ID integer cleanly from the unit object
    iPlayer = pUnit.getOwner()
    pPlayer = gc.getPlayer(iPlayer)
    
    if pPlayer is None or pPlayer.isNone() or not pPlayer.isHuman():
        return gameUtils().doGoody(argsList)
        
    szGoodyTypeStr = gc.getGoodyInfo(eGoodyType).getType()
    
    # If the engine selected a technology reward for the human under Techsanity settings
    import ArchipelagoData
    if szGoodyTypeStr == "GOODY_TECH" and ArchipelagoData.archipelagoTechsanityEnabled:
        # Re-roll a random alternative goody entry that IS NOT a technology!
        validAlternatives = ["GOODY_LOW_GOLD", "GOODY_HIGH_GOLD", "GOODY_MAP", "GOODY_EXPERIENCE"]
        
        # Pick a random item from our list using the engine's synchronized dice roller
        iRandomIndex = gc.getGame().getSorenRandNum(len(validAlternatives), "Archipelago Hut Re-roll")
        szSelectedGoody = validAlternatives[iRandomIndex]
        
        eNewGoody = gc.getInfoTypeForString(szSelectedGoody)
        
        if eNewGoody != -1:
            # Overwrite the original index value in the event array argument slice!
            # Python allows mutable list mutation-altering argsList changes the payload 
            # the C++ engine uses to deliver the item on this frame pass.
            argsList[0] = eNewGoody
            
    # Forward the modified argsList payload cleanly to the native engine rules handler
    return gameUtils().doGoody(argsList)


def doGrowth(argsList):
    #CvUtil.pyPrint( "CvGameInterface.doGrowth" )
    return gameUtils().doGrowth(argsList)

def doProduction(argsList):
    #CvUtil.pyPrint( "CvGameInterface.doProduction" )
    return gameUtils().doProduction(argsList)

def doCulture(argsList):
    #CvUtil.pyPrint( "CvGameInterface.doCulture" )
    return gameUtils().doCulture(argsList)

def doPlotCulture(argsList):
    #CvUtil.pyPrint( "CvGameInterface.doPlotCulture" )
    return gameUtils().doPlotCulture(argsList)

def doReligion(argsList):
    #CvUtil.pyPrint( "CvGameInterface.doReligion" )
    return gameUtils().doReligion(argsList)

def doGreatPeople(argsList):
    #CvUtil.pyPrint( "CvGameInterface.doGreatPeople" )
    return gameUtils().doGreatPeople(argsList)

def doMeltdown(argsList):
    #CvUtil.pyPrint( "CvGameInterface.doMeltdown" )
    return gameUtils().doMeltdown(argsList)

def doReviveActivePlayer(argsList):
    return gameUtils().doReviveActivePlayer(argsList)

def doPillageGold(argsList):
    return gameUtils().doPillageGold(argsList)

def doCityCaptureGold(argsList):
    return gameUtils().doCityCaptureGold(argsList)

def citiesDestroyFeatures(argsList):
    return gameUtils().citiesDestroyFeatures(argsList)

def canFoundCitiesOnWater(argsList):
    return gameUtils().canFoundCitiesOnWater(argsList)

def doCombat(argsList):
    return gameUtils().doCombat(argsList)

def getConscriptUnitType(argsList):
    return gameUtils().getConscriptUnitType(argsList)

def getCityFoundValue(argsList):
    return gameUtils().getCityFoundValue(argsList)

def canPickPlot(argsList):
    return gameUtils().canPickPlot(argsList)

def getUnitCostMod(argsList):
    return gameUtils().getUnitCostMod(argsList)

def getBuildingCostMod(argsList):
    return gameUtils().getBuildingCostMod(argsList)

def canUpgradeAnywhere(argsList):
    return gameUtils().canUpgradeAnywhere(argsList)

def getWidgetHelp(argsList):
    return gameUtils().getWidgetHelp(argsList)

def getUpgradePriceOverride(argsList):
    return gameUtils().getUpgradePriceOverride(argsList)

def getExperienceNeeded(argsList):
    return gameUtils().getExperienceNeeded(argsList)
