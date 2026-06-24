from CvPythonExtensions import *
import CvUtil

# Global instance tracker
g_ArchipelagoConsole = None

class ArchipelagoConsole:
    def __init__(self):
        self.SCREEN_NAME = "ArchipelagoConsoleWindow"
        self.W_SCREEN = 500
        self.H_SCREEN = 450
        
    def getScreen(self):
        return CyGInterfaceScreen(self.SCREEN_NAME, CvPythonExtensionsWidgetDataValues.WIDGET_GENERAL)

    def interfaceScreen(self):
        screen = self.getScreen()
        if screen.isActive():
            return

        # Calculate centering coordinates on user's monitor
        x_pos = (screen.getXResolution() / 2) - (self.W_SCREEN / 2)
        y_pos = (screen.getYResolution() / 2) - (self.H_SCREEN / 2)

        # 1. Initialize the Master Screen Dialog Window
        screen.setDimensions(x_pos, y_pos, self.W_SCREEN, self.H_SCREEN)
        screen.showScreen(PopupStates.POPUP_STATE_IMMEDIATE, False)
        
        # 2. Draw a standard Civ4 decorated panel background frame
        screen.addPanel("ConsoleBg", u"", u"", True, False, 0, 0, self.W_SCREEN, self.H_SCREEN, PanelStyles.PANEL_STYLE_MAIN)
        screen.addDrawControl("ConsoleBg", "Art/Interface/Screens/City_Management/Building_Background.dds", 0, 0, self.W_SCREEN, self.H_SCREEN, WidgetTypes.WIDGET_GENERAL, -1, -1)
        
        # Header title text string line
        screen.setLabel("ConsoleHeader", "ConsoleBg", u"<font=4b>Archipelago Server Log</font>", CvUtil.FONT_CENTER_JUSTIFY, self.W_SCREEN / 2, 15, -0.1, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)

        # 3. Create the pixel-perfect Fixed Scroll Panel
        # Arguments: (PanelID, TitleText, X, Y, Width, Height, Style)
        scroll_panel_id = "ConsoleScrollBox"
        panel_w = self.W_SCREEN - 40   # 460 pixels wide
        panel_h = self.H_SCREEN - 120  # 330 pixels tall
        screen.addScrollPanel(scroll_panel_id, u"", 20, 50, panel_w, panel_h, PanelStyles.PANEL_STYLE_EXTERNAL)

        # 4. Populate with coordinates to force independent scrollbar tracking
        line_height = 22
        for i in range(50):
            label_id = f"ConsoleLine_{i}"
            text_string = f"Server Packet Line Tracker Log Entry #{i}"
            
            # Local position matching the exact pixel index inside the viewport tracking box
            local_x = 10
            local_y = i * line_height
            
            # Using absolute coordinate binding for child entries inside the viewport
            screen.setTextAt(label_id, scroll_panel_id, text_string, CvUtil.FONT_LEFT_JUSTIFY, local_x, local_y, -0.1, FontTypes.SMALL_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)

        # 5. Add a Close Button at the bottom
        screen.setButtonGFC("CloseConsoleBtn", u"Close Window", "", (self.W_SCREEN / 2) - 60, self.H_SCREEN - 50, 120, 30, WidgetTypes.WIDGET_CLOSE_SCREEN, -1, -1, ButtonStyles.BUTTON_STYLE_STANDARD)

def showConsole():
    global g_ArchipelagoConsole
    if g_ArchipelagoConsole is None:
        g_ArchipelagoConsole = ArchipelagoConsole()
    g_ArchipelagoConsole.interfaceScreen()
