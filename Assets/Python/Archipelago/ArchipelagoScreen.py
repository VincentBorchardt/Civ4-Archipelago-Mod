from CvPythonExtensions import *
import CvUtil
import BugOptions
import ArchipelagoItems
import ArchipelagoStuff

gc = CyGlobalContext()

class ArchipelagoConnectionScreen:
    def __init__(self):
        self.SCREEN_NAME = "ArchipelagoConnectionScreen"
        self.EDIT_SERVER_NAME = "ApEditServer"
        self.EDIT_USER_NAME = "ApEditUser"
        self.EDIT_PASS_NAME = "ApEditPass"
        
        # Unique tracking IDs to force keyboard focus and click capture
        self.ID_SERVER = 6001
        self.ID_USER = 6002
        self.ID_PASS = 6003
        self.ID_BTN = 6004

    def getScreen(self):
        return CyGInterfaceScreen(self.SCREEN_NAME, 5000)

    def interfaceScreen(self, failedConnection=False):
        screen = self.getScreen()
        if screen.isActive():
            return

        # Define sizes relative to resolution center
        iWidth = 400
        iHeight = 300
        iX = screen.getXResolution() / 2 - (iWidth / 2)
        iY = screen.getYResolution() / 2 - (iHeight / 2)

        # 1. Open layout canvas window bounds
        screen.setDimensions(iX, iY, iWidth, iHeight)
        screen.showScreen(PopupStates.POPUPSTATE_IMMEDIATE, False)
        
        screen.setRenderInterfaceOnly(False)
        screen.setCloseOnEscape(True)

        # 2. Draw background panel frame at base coordinate origin (0, 0)
        screen.addPanel("ApBackground", "", "", True, False, 0, 0, iWidth, iHeight, PanelStyles.PANEL_STYLE_MAIN)
        
        # 3. All child elements are nested inside "ApBackground" using LOCAL coordinates (relative to 400x300 container)
        if failedConnection:
            screen.setLabel("ApHeader", "ApBackground", "<color=255,0,0>Connection Failed!</color>", CvUtil.FONT_CENTER_JUSTIFY, 200, 20, 0, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)
        else:
            screen.setLabel("ApHeader", "ApBackground", "Archipelago Setup", CvUtil.FONT_CENTER_JUSTIFY, 200, 20, 0, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)

        server = BugOptions.getOption("Archipelago__ArchipelagoServer").getValue()
        username = BugOptions.getOption("Archipelago__ArchipelagoUsername").getValue()
        password = BugOptions.getOption("Archipelago__ArchipelagoPassword").getValue()

        # Labels and Edit Boxes mapped safely inside the panel container
        screen.setLabel("LblServer", "ApBackground", "Server IP/Port:", CvUtil.FONT_LEFT_JUSTIFY, 30, 70, 0, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)
        screen.addEditBoxGFC(self.EDIT_SERVER_NAME, 180, 65, 190, 30, WidgetTypes.WIDGET_GENERAL, self.ID_SERVER, -1, FontTypes.GAME_FONT)
        screen.setEditBoxString(self.EDIT_SERVER_NAME, server)

        screen.setLabel("LblUser", "ApBackground", "Slot Username:", CvUtil.FONT_LEFT_JUSTIFY, 30, 120, 0, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)
        screen.addEditBoxGFC(self.EDIT_USER_NAME, 180, 115, 190, 30, WidgetTypes.WIDGET_GENERAL, self.ID_USER, -1, FontTypes.GAME_FONT)
        screen.setEditBoxString(self.EDIT_USER_NAME, username)

        screen.setLabel("LblPass", "ApBackground", "Room Password:", CvUtil.FONT_LEFT_JUSTIFY, 30, 170, 0, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)
        screen.addEditBoxGFC(self.EDIT_PASS_NAME, 180, 165, 190, 30, WidgetTypes.WIDGET_GENERAL, self.ID_PASS, -1, FontTypes.GAME_FONT)
        screen.setEditBoxString(self.EDIT_PASS_NAME, password)

        # 4. Connect Button mapped using correct ButtonStyles enum and explicit tracking ID allocation
        screen.setButtonGFC("BtnConnect", "Connect", "Art/Interface/Buttons/Actions/Join.dds", 150, 230, 100, 30, WidgetTypes.WIDGET_GENERAL, self.ID_BTN, -1, ButtonStyles.BUTTON_STYLE_STANDARD)

    def handleInput(self, inputClass):
        """Monitors keystrokes and selection confirmations."""
        # Route logic using our explicit ID allocation to guarantee click capture
        if inputClass.getFunctionName() == "BtnConnect" or inputClass.getData1() == self.ID_BTN:
            if inputClass.getNotifyCode() == NotifyCode.NOTIFY_CLICKED:
                screen = self.getScreen()
                
                szServer = screen.getEditBoxString(self.EDIT_SERVER_NAME)
                szUsername = screen.getEditBoxString(self.EDIT_USER_NAME)
                szPassword = screen.getEditBoxString(self.EDIT_PASS_NAME)

                BugOptions.getOption("Archipelago__ArchipelagoServer").setValue(szServer)
                BugOptions.getOption("Archipelago__ArchipelagoUsername").setValue(szUsername)
                BugOptions.getOption("Archipelago__ArchipelagoPassword").setValue(szPassword)

                ArchipelagoStuff.connectToArchipelago(szServer, szUsername, szPassword)

                if ArchipelagoItems.is_connected_to_ap:
                    screen.hideScreen()
                else:
                    self.interfaceScreen(failedConnection=True)
                    
        return 0
