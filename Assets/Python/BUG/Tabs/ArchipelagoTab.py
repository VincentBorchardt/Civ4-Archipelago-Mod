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
        
        # PART 3: The Bounded Scrollable Text Log Area
        # We declare a unique string name for our target text log viewport container
        logPanelName = "ApLogScrollBox"
        
        # FIX: Force the right stack column to lock its vertical dimensions!
        # This keeps the master window stable and forces scroll panes to clip.
        screen.setColumnLength(320)
        
        # PART 3: The Bounded Scrollable Text Log Area
        logPanelName = "ApLogScrollBox"
        screen.attachScrollPanel(rightStack, logPanelName)
        
        # FIX: Force the interior scroll panel container to expand to fill the right column limits
        screen.setLayoutFlag(logPanelName, "LAYOUT_SIZE_RESIZABLE")
        
        # CRUCIAL HOOK: To place things inside the scroll area, the parent container string 
        # passed to your labels must be your new logPanelName variable!
        for i in range(0, 50):
            label_id = "LogMsg" + str(i)
            screen.attachLabel(logPanelName, label_id, "Server Packet Line Tracker Log Entry #" + str(i))
            screen.setLayoutFlag(label_id, "LAYOUT_SIZE_RESIZABLE")


        # DRAW VISUAL DIVIDER ABOVE COMMAND PROMPT
        screen.attachHSeparator(rightStack, rightStack + "Sep1")
        
        # Command input text line box entry at the very bottom right
        colL3, colR3 = self.addTwoColumnLayout(screen, rightStack, "TerminalSettings")
        
        # Map a raw text edit box straight to a custom data caching option string slot
        self.addTextEdit(screen, colL3, colR3, "Archipelago__ArchipelagoCommand")
