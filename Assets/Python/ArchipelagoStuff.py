from CvPythonExtensions import *
from PyHelpers import *
from Popup import PyPopup

import socket

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

def connectToArchipelagoServer(server, username, password):
	#modPopup = PyPopup()
	#modPopup.setHeaderString(server)
	#modPopup.setBodyString(username)
	#modPopup.launch()
	client_program(server, username, password)

def client_program(server, username, password):
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = server  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        modPopup = PyPopup()
	modPopup.setHeaderString("recieved data")
	modPopup.setBodyString(data)
	modPopup.launch()

        #print('Received from server: ' + data)  # show in terminal

        message = 'bye'  # again take input

    client_socket.close()  # close the connection
			
	

