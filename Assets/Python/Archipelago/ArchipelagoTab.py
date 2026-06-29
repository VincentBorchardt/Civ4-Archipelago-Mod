## ArchipelagoTab.py
## UI Layout Handler module for the Civilization 4 Archipelago Mod config tabs

from CvPythonExtensions import *
import CvUtil

import BugOptionsTab
import BugOptions
import BugOptionsScreen

import ArchipelagoStuff
import ArchipelagoData

class ArchipelagoTab(BugOptionsTab.BugOptionsTab):
    """Governs drawing, element arrangement, and layout rendering calculations."""
    
    def __init__(self, screen):
        BugOptionsTab.BugOptionsTab.__init__(self, "ArchipelagoTab", "Archipelago Options")

    def create(self, screen):
        screen.setSize(1200, 800)
        
        """Executes rendering instructions using BUG's strict initialization hook."""
        tab = self.createTab(screen)
        panel = self.createMainPanel(screen)

        
        # MAIN GRID: Split Left Half and Right Half
        mainLeft, mainRight = self.addTwoColumnLayout(screen, panel, "MainGrid", separator=True)

        # LEFT HALF STACK
        leftStack = self.addOneColumnLayout(screen, mainLeft)

        # PART 1: Upper Left - Connection Box
        colL1, colR1 = self.addTwoColumnLayout(screen, leftStack, "ServerSettings")
        self.addTextEdit(screen, colL1, colR1, "Archipelago__ArchipelagoServer")
        self.addTextEdit(screen, colL1, colR1, "Archipelago__ArchipelagoUsername")
        self.addTextEdit(screen, colL1, colR1, "Archipelago__ArchipelagoPassword")
        self.addButton(screen, colL1, "BtnConnect", "onConnectClicked", "Save and Connect")

        # DRAW VISUAL DIVIDER LINE BETWEEN UPPER AND LOWER LEFT PANELS
        screen.attachHSeparator(leftStack, leftStack + "Sep1")


        # PART 2: Lower Left - Gameplay settings
        colL2, colR2 = self.addTwoColumnLayout(screen, leftStack, "ArchipelagoSettings")
        self.addCheckbox(screen, colL2, "Archipelago__ShowAnnouncements")
        self.addButton(screen, colL2, "BtnSync", "onSyncClicked", "Manual Sync")
        #self.addLabel(screen, colL2, "OptionsLabel", "Options / Toggles Placeholder")


        # RIGHT HALF STACK: The Console Area
        rightStack = self.addOneColumnLayout(screen, mainRight)

        #self.addLabel(screen, rightStack, "ConsoleInfoLabel", "View Archipelago Message Log:")
        #self.addButton(screen, rightStack, "BtnOpenConsole", "onOpenConsoleClicked", "Open Full Console Log Window")

        colL3, colC3, colR3 = self.addThreeColumnLayout(screen, rightStack, "CommandSending")
        self.addTextEdit(screen, colL3, colC3, "Archipelago__ArchipelagoCommand")
        self.addButton(screen, colR3, "BtnSendCommand", "onSendCommandClicked", "Send Command")
                                                        
        self.addButton(screen, rightStack, "BtnRefreshHints", "onRefreshHintsClicked", "Refresh Hints")
        
        screen.attachHSeparator(rightStack, rightStack + "Sep1")

        hintsList = ArchipelagoData.archipelagoHints

        
        if not hintsList:
            # Baseline placeholder view if the player hasn't pressed sync yet
            self.addLabel(screen, rightStack, "NoHintsLbl", "No hint data cached.")
        else:
            # Generate a multi-column row grid block inside BUG's layout sheet
            # By passing count=7, every 7 labels we append will naturally wrap into a perfect row
            grid = self.addMultiColumnLayout(screen, rightStack, 7, "HintGridTable", separator=True)
            
            # 1. DRAW ROW 0: HEADERS (Enclosed in uppercase yellow text tags)
            headers = ["Receiver", "Item", "Type", "Finder", "Location", "Entrance", "Status"]
            for i in range(0, len(headers)):
                self.addLabel(screen, grid[i], "Hdr_" + headers[i], headers[i])
            
            # 2. DRAW ROWS 1+: STREAM DATA DYNAMICALLY
            row_index = 0
            for hint in hintsList:
                szReceiver = str(hint.get("receiving_player", "Unknown"))
                szItem = str(hint.get("item", "Unknown"))
                szType = str(hint.get("item_type", "Normal"))
                szFinder = str(hint.get("finding_player", "Unknown"))
                szLocation = str(hint.get("location", "Unknown"))
                szEntrance = str(hint.get("entrance", "Vanilla"))
                szStatus = str(hint.get("status", "Unspecified"))
                
                
                # Append elements sequentially; the engine handles columns 1-7 layout properties for us!
                self.addLabel(screen, grid[0], "HintRecv_" + str(row_index), szReceiver)
                self.addLabel(screen, grid[1], "HintItem_" + str(row_index), szItem)
                self.addLabel(screen, grid[2], "HintType_" + str(row_index), szType)
                self.addLabel(screen, grid[3], "HintFind_" + str(row_index), szFinder)
                self.addLabel(screen, grid[4], "HintLoc_" + str(row_index), szLocation)
                self.addLabel(screen, grid[5], "HintEnt_" + str(row_index), szEntrance)
                self.addLabel(screen, grid[6], "HintStat_" + str(row_index), szStatus)
                
                row_index += 1
