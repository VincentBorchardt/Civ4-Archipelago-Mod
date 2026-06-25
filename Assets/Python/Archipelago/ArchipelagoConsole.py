from CvPythonExtensions import *
import CvUtil
import BugOptionsScreen

# Global instance tracker
g_ArchipelagoConsole = None

class ArchipelagoConsole:
    def __init__(self):
        self.SCREEN_NAME = "ArchipelagoConsoleWindow"
        self.W_SCREEN = 550
        self.H_SCREEN = 540 # Increased height to easily trap text and scroll boundaries
        
    def getScreen(self):
        return CyGInterfaceScreen(self.SCREEN_NAME, WidgetTypes.WIDGET_GENERAL)

    def interfaceScreen(self):
        screen = self.getScreen()
        if screen.isActive():
            return

        # 1. Close the BUG Options window safely
        if BugOptionsScreen.g_optionsScreen is not None:
            BugOptionsScreen.g_optionsScreen.close()

        # Center layout coordinates on monitor
        x_pos = (screen.getXResolution() / 2) - (self.W_SCREEN / 2)
        y_pos = (screen.getYResolution() / 2) - (self.H_SCREEN / 2)

        # 2. Initialize Master Dialog Screen Canvas
        screen.setDimensions(x_pos, y_pos, self.W_SCREEN, self.H_SCREEN)
        screen.showScreen(PopupStates.POPUPSTATE_IMMEDIATE, False)
        
        # 3. DRAW STYLING: Game-Themed Outer Panel with Borders
        screen.addPanel("ConsoleMainBg", "", "", True, False, 0, 0, self.W_SCREEN, self.H_SCREEN, PanelStyles.PANEL_STYLE_MAIN)
        screen.setLabel("ConsoleHeader", "ConsoleMainBg", "<font=4b>Archipelago Server Log</font>", CvUtil.FONT_CENTER_JUSTIFY, self.W_SCREEN / 2, 15, -0.1, FontTypes.GAME_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)

        # 4. SCROLL PANEL DIMENSION AND OVERFLOW FIX
        # Background panels are expanded vertically to eliminate text spilling over the bottom margins
        scroll_panel_id = "ConsoleScrollBox"
        panel_w = self.W_SCREEN - 40   # 510 pixels wide
        panel_h = self.H_SCREEN - 150  # 390 pixels tall (perfect container constraint)
        
        screen.addPanel("ScrollPanelInset", "", "", True, True, 20, 50, panel_w, panel_h, PanelStyles.PANEL_STYLE_IN)
        screen.addScrollPanel(scroll_panel_id, "", 20, 50, panel_w - 5, panel_h - 25, PanelStyles.PANEL_STYLE_EXTERNAL)

        # Raw log lines example array
        raw_logs = [
            "Server Packet Line Tracker Log Entry " + str(i) + " - This is a very long log string intended to test the smart local string splitting text wrap features inside the Civ4 Python 2.4 compiler constraints safely without dividing words or clipping!"
            for i in range(25)
        ]

        # 5. SMART WORD-WRAPPING (Python 2.4 Compatible)
        MAX_CHARS_PER_LINE = 75 
        processed_lines = []
        
        for long_line in raw_logs:
            words = long_line.split(" ")
            current_line = ""
            
            for word in words:
                # Check if adding the next word exceeds our safe column pixel width
                if len(current_line) + len(word) + 1 <= MAX_CHARS_PER_LINE:
                    if current_line == "":
                        current_line = word
                    else:
                        current_line += " " + word
                else:
                    # Push line out and start a fresh one for the overflowing word
                    processed_lines.append(current_line)
                    current_line = word
            
            if current_line:
                processed_lines.append(current_line)

        # Draw the neatly wrapped lines to the viewport coordinates
        line_height = 22
        for i, line_text in enumerate(processed_lines):
            label_id = "ConsoleLine_" + str(i)
            local_x = 10
            local_y = i * line_height
            screen.setTextAt(label_id, scroll_panel_id, line_text, CvUtil.FONT_LEFT_JUSTIFY, local_x, local_y, -0.1, FontTypes.SMALL_FONT, WidgetTypes.WIDGET_GENERAL, -1, -1)

        # 6. INPUT COMMAND PROMPT STRIP (Utilizing your verified signature line!)
        input_y = self.H_SCREEN - 95
        edit_box_w = self.W_SCREEN - 150 
        
        screen.addEditBoxGFC("ApConsoleInputField", 20, input_y, edit_box_w, 30, WidgetTypes.WIDGET_GENERAL, 1, 1, FontTypes.GAME_FONT)
        screen.setButtonGFC("SendConsoleCmdBtn", "Send", "", 20 + edit_box_w + 10, input_y, 100, 30, WidgetTypes.WIDGET_GENERAL, -1, -1, ButtonStyles.BUTTON_STYLE_STANDARD)

        # 7. BOTTOM CLOSE WINDOW ACTION BUTTON
        screen.setButtonGFC("CloseConsoleBtn", "Close Window", "", (self.W_SCREEN / 2) - 60, self.H_SCREEN - 50, 120, 30, WidgetTypes.WIDGET_GENERAL, -1, -1, ButtonStyles.BUTTON_STYLE_STANDARD)

    def handleInput(self, szFunctionName):
        """Processes clicking events via verified string lookup."""
        screen = self.getScreen()
        
        if szFunctionName == "CloseConsoleBtn":
            screen.hideScreen()
            if BugOptionsScreen.g_optionsScreen is not None:
                BugOptionsScreen.g_optionsScreen.interfaceScreen()
            return 1
            
        elif szFunctionName == "SendConsoleCmdBtn":
            command_text = screen.getEditBoxString("ApConsoleInputField")
            screen.setEditBoxString("ApConsoleInputField", "")

            CyInterface().addImmediateMessage("Archipelago Command Transmitted: " + str(command_text), "")
            return 1
            
        return 0

def showConsole():
    global g_ArchipelagoConsole
    if g_ArchipelagoConsole is None:
        g_ArchipelagoConsole = ArchipelagoConsole()
    g_ArchipelagoConsole.interfaceScreen()

def handleConsoleInput(argsList):
    """Parses raw argsList tuple data without throwing NameErrors."""
    global g_ArchipelagoConsole
    if g_ArchipelagoConsole and g_ArchipelagoConsole.getScreen().isActive():
        # Safeguard array sizing limits
        if len(argsList) > 5:
            szFunctionName = argsList[5] # Index 5 is the text name of the clicked component
            return g_ArchipelagoConsole.handleInput(szFunctionName)
    return 0
