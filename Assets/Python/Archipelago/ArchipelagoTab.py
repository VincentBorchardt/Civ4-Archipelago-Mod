## ArchipelagoTab.py
## UI Layout Handler module for the Civilization 4 Archipelago Mod config tabs

from CvPythonExtensions import *
import CvUtil

import BugOptionsTab
import BugOptions

class ArchipelagoTab(BugOptionsTab.BugOptionsTab):
    """Governs drawing, element arrangement, and layout rendering calculations."""
    
    def __init__(self, screen):
        BugOptionsTab.BugOptionsTab.__init__(self, "ArchipelagoTab", "Archipelago Options")

    def create(self, screen):
        """Executes rendering instructions using BUG's strict initialization hook."""
        tab = self.createTab(screen)
        panel = self.createMainPanel(screen)

        # 1. DIVIDING LINE TECHNIQUE: How BUG makes section lines
        # Drawing a blank label with a styled underline creates a vertical or horizontal line.
        # Passing an explicit rule name allows BUG's layout sheet to space it.
        
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
        self.addLabel(screen, colL2, "OptionsLabel", "Options / Toggles Placeholder")


        # RIGHT HALF STACK: The Console Area
        rightStack = self.addOneColumnLayout(screen, mainRight)
        
        screen.attachHSeparator(rightStack, rightStack + "Sep1")
        
        self.addLabel(screen, rightStack, "ConsoleInfoLabel", "View Archipelago Message Log:")
        self.addButton(screen, rightStack, "BtnOpenConsole", "onOpenConsoleClicked", "Open Console Log Window")
