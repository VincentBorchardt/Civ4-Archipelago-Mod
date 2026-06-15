from CvPythonExtensions import *
from PyHelpers import *
from Popup import PyPopup

import BugOptions

import socket
import errno

# TODO NEED TO EVENTUALLY IMPLEMENT A SAFE UNPICKLER!!!
import pickle

# constants
gc = CyGlobalContext()
cyGame = CyGame()
cyMap = CyMap()
pyGame = PyGame()

popupHeader = "Tutorial"
popupMessage = "This is a Python tutorial.\n\nby Baldyr"

socket_to_archipelago = socket.socket()  # instantiate
socket_to_archipelago.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # enable address reuse

def showPopup(header=popupHeader, body=popupMessage):
	modPopup = PyPopup()
	modPopup.setHeaderString(header)
	modPopup.setBodyString(body)
	modPopup.launch()

def checkForReads():
    # The AI does a defensive check here; I don't think I care (and it's not accurate anyway)

    try:
        data_pickle = socket_to_archipelago.recv(1024)  # receive response
        if data_pickle:
            data_dict = pickle.loads(data_pickle)
            if data_dict["cmd"] == "Connected":
                showPopup("Connected", "Successfully Connected")
    except socket.error, e: # Python 2.4 comma syntax
        err_code = e[0]
        # If the code is just "no data available right now", release control
        if err_code in (errno.EWOULDBLOCK, errno.EAGAIN, 10035):
            return None 

def sendAndReceiveData(messageDict):
    messagePickle = pickle.dumps(messageDict, 2)

def connectToArchipelagoServer(server, username, password):
    if server == "":
        showPopup("Connection Error", "Please enter a server name.")
        return
    if username == "":
        showPopup("Connection Error", "Please enter a slot name.")
        return
    # TODO Should check if all fields have any characters that will cause parsing errors
    BugOptions.getOption("Archipelago__ArchipelagoServer").setValue(server)
    BugOptions.getOption("Archipelago__ArchipelagoUsername").setValue(username)
    BugOptions.getOption("Archipelago__ArchipelagoPassword").setValue(password)
    
    
    #try: # Not sure what error to try and catch for "connection refused"--it's "10061" on Windows 11
    socket_to_archipelago = socket.socket()  # instantiate
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    socket_to_archipelago.connect((host, port))  # connect to the server

    messageDict = { "type":"connect", "server":server, "username":username, "password":password }
    messagePickle = pickle.dumps(messageDict, 2)

    socket_to_archipelago.sendall(messagePickle)  # send message

    try:
        data_pickle = socket_to_archipelago.recv(1024)  # receive response
        if data_pickle:
            data_dict = pickle.loads(data_pickle)
            if data_dict["cmd"] == "Connected":
                showPopup("Connected", "Successfully Connected")
    except socket.error, e: # Python 2.4 comma syntax
        err_code = e[0]
        # If the code is just "no data available right now", release control
        if err_code in (errno.EWOULDBLOCK, errno.EAGAIN, 10035):
            return None
    
    #showPopup("Received Data", data)

    #except Error:

def disconnectFromArchipelagoServer():
    #if not isSocketConnected():
        #showPopup("Connection Error", "Not connected to a server")
        #return
    try:
        socket_to_archipelago.settimeout(3.0)
        socket_to_archipelago.shutdown(socket.SHUT_RDWR)
    except Exception, e:
        showPopup("Shutdown Error", str(e))
    showPopup("after shutdown", "test")
    socket_to_archipelago.close()
    showPopup("after close", "test")
    return
    
            


			
	

