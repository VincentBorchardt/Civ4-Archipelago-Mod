from CvPythonExtensions import *
from PyHelpers import *
from Popup import PyPopup

# constants
gc = CyGlobalContext()
cyGame = CyGame()
cyMap = CyMap()
pyGame = PyGame()

iPropability = 5
eBarbarian = gc.getBARBARIAN_PLAYER()
pyBarbarian = PyPlayer(eBarbarian)
popupHeader = "Tutorial"
popupMessage = "This is a Python tutorial.\n\nby Baldyr"

# show popup

modPopup = PyPopup()
modPopup.setHeaderString(popupHeader)
modPopup.setBodyString(popupMessage)
modPopup.launch()
