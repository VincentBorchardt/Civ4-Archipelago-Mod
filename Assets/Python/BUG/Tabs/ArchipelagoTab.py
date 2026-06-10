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

        # FIX: Point the callback directly to an action function inside this module file
        # Syntax: self.addButton(screen, layoutContainer, "Module.Function", "Button Display Text")
        self.addButton(screen, columnL, "Connect", "ArchipelagoTab.onConnectClicked", )
        self.addButton(screen, columnL, "Disconnect", "ArchipelagoTab.onDisconnectClicked")

    def onConnectClicked(self, screen, button):
        # This will now fire properly!
        screen.updateOptions()

        # BugOptions is completely valid here if defined in your XML data sections
        server = BugOptions.getOption("Archipelago__ArchipelagoServer").getValue()
        username = BugOptions.getOption("Archipelago__ArchipelagoUsername").getValue()
        password = BugOptions.getOption("Archipelago__ArchipelagoPassword").getValue()

        ArchipelagoStuff.connectToArchipelagoServer(server, username, password)
        
    def onDisconnectClicked(self, screen, button):
        # Add your disconnect handler logic here
        pass
