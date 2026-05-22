from CvPythonExtensions import *
from PyHelpers import *
from Popup import PyPopup

# constants
gc = CyGlobalContext()
cyGame = CyGame()
cyMap = CyMap()
pyGame = PyGame()

popupHeader = "Tutorial"
popupMessage = "This is a Python tutorial.\n\nby Baldyr"

def showPopup():
	"""Displays the welcome message on game start"""
	modPopup = PyPopup()
	modPopup.setHeaderString(popupHeader)
	modPopup.setBodyString(popupMessage)
	modPopup.launch()

def checkIfArchipelagoTech(tech):
	showPopup()
	
	tech_info = gc.getTechInfo(tech)
    
	# FLAVOR_ARCHIPELAGO is FlavorValue(8); currently hardcoded
	flavor_weight = tech_info.getFlavorValue(8)
        if flavor_weight > 0:
		modPopupA = PyPopup()
		modPopupA.setHeaderString("This is an Archipelago Tech")
		modPopupA.setBodyString(popupMessage)
		modPopupA.launch()
			
	
	
