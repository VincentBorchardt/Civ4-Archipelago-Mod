## ArchipelagoTab.py
## UI Layout Handler module for the Civilization 4 Archipelago Mod config tabs

from CvPythonExtensions import *
import BugOptionsTab
import BugOptions


import ArchipelagoStuff

class ArchipelagoTab(BugOptionsTab.BugOptionsTab):
    """Governs drawing, element arrangement, and layout rendering calculations."""
    
    def __init__(self, screen):
        # Initialize the baseline BUG panel parameters natively
        BugOptionsTab.BugOptionsTab.__init__(self, "ArchipelagoTab", "Archipelago Options")

    def create(self, screen):
        """Executes rendering instructions using BUG's strict initialization hook."""
        # 1. Establish the basic tab layout sheet frame inside parent memory
        tab = self.createTab(screen)
        
        # 2. Render the visual grouping panel container
        panel = self.createMainPanel(screen)

        column = self.addOneColumnLayout(screen, panel)

        columnL, columnR = self.addTwoColumnLayout(screen, column, "ServerSettings")
        
        # 3. Add your elements using your working storage mapping: ModID__SettingName
        self.addTextEdit(screen, columnL, columnR, "Archipelago__ArchipelagoServer")
        self.addTextEdit(screen, columnL, columnR, "Archipelago__ArchipelagoUsername")
        self.addTextEdit(screen, columnL, columnR, "Archipelago__ArchipelagoPassword")

        self.addButton(screen, columnL, "onConnectClicked", "Connect")
        self.addButton(screen, columnL, "onDisconnectClicked", "Disconnect")

    def onConnectClicked(self, screen, button):
        screen.updateOptions()

        # LOCAL IMPORT: This avoids the ConfigError crash during game boot!
        #import BugCore

        server = BugOptions.getOption("Archipelago__ArchipelagoServer").getValue()
        username = BugOptions.getOption("Archipelago__ArchipelagoUsername").getValue()
        password = BugOptions.getOption("Archipelago__ArchipelagoPassword").getValue()

        ArchipelagoStuff.connectToArchipelagoServer(server, username, password)
        

    def onDisconnectClicked(self, screen, button):
        pass
