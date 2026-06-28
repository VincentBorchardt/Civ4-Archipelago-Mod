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

        self.addButton(screen, rightStack, "BtnRefreshHints", "onRefreshHintsClicked", "Refresh Hints")
        
        screen.attachHSeparator(rightStack, rightStack + "Sep1")

        hintsList = ArchipelagoData.archipelagoHints
        
        if not hintsList:
            # Baseline placeholder view if the player hasn't pressed sync yet
            self.addLabel(screen, rightStack, "NoHintsLbl", "No hint data cached.")
        else:
            self.addLabel(screen, rightStack, "HintHeader", "<color=255,255,0>Archipelago Hints Received From Server:</color>")
            screen.attachHSeparator(rightStack, "RightHeaderSep")
            
            # Create a 4-Column Layout grid box using BUG's built-in column generator
            gridL, gridR = self.addTwoColumnLayout(screen, rightStack, "HintGrid")
            
            row_index = 0
            for hint in hintsList:
                szItem = str(hint.get("item", "Unknown"))
                szType = str(hint.get("item_type", "Normal"))
                szFinder = str(hint.get("finding_player", "Unknown"))
                szLocation = str(hint.get("location", "Unknown"))
                
                # If it's a vital progression item, wrap it in a teal text tag
                if szType == "Progression":
                    szItem = "<color=0,255,255>" + szItem + "</color>"
                
                # Combine the strings into readable, flat label segments
                # Because we are using the two-column grid layout, dropping these two lines 
                # sequentially places the Item/Type on the Left, and Finder/Location on the Right
                leftLabelText = "%s (%s)" % (szItem, szType)
                rightLabelText = "Found by %s at %s" % (szFinder, szLocation)
                
                # Render using standard, un-nestable BUG labels with unique tracking IDs
                self.addLabel(screen, gridL, "HintItem_" + str(row_index), leftLabelText)
                self.addLabel(screen, gridR, "HintLoc_" + str(row_index), rightLabelText)
                
                row_index += 1

    def refreshHints(self):
        optionsScreen = BugOptionsScreen.g_optionsScreen
        if optionsScreen is not None:
            # Force-close the active UI window
            optionsScreen.hideScreen()
            
            # Re-open it immediately! This re-triggers the create() loop on your tab,
            # forcing it to find your fresh archipelagoHints data and draw the new labels instantly.
            optionsScreen.interfaceScreen()
            
