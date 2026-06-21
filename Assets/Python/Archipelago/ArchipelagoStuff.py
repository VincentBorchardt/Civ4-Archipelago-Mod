from CvPythonExtensions import *
import CvUtil
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

hasConnectedToArchipelago = False
isConnectedToArchipelago = False

socket_to_archipelago = socket.socket()
socket_to_archipelago.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # enable address reuse

# TODO Use the message log for some of this stuff rather than PyPopup
def showPopup(header=popupHeader, body=popupMessage):
	modPopup = PyPopup()
	modPopup.setHeaderString(header)
	modPopup.setBodyString(body)
	modPopup.launch() 

# TODO do I want to decouple sending and receiving?
# Manually doing a socket every time seems wasteful, but it's a later optimization
def sendAndReceiveData(messageDict, waitForRead=True):
    messagePickle = pickle.dumps(messageDict, 2)

    socket_to_archipelago = socket.socket()  # instantiate
    socket_to_archipelago.settimeout(2.0)
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    # OUTER TRY: Handles only the finally cleanup in Python 2.4
    try:
        # INNER TRY: Handles the execution and exception catching
        try:
            socket_to_archipelago.connect((host, port))  # connect to the server
            socket_to_archipelago.sendall(messagePickle)  # send message

            isConnectedToArchipelago = True
            hasConnectedToArchipelago = True

            if waitForRead:
                data_pickle = socket_to_archipelago.recv(1024)
                if data_pickle:
                    data_dict = pickle.loads(data_pickle)
                    if isinstance(data_dict, dict) and "cmd" in data_dict:
                        return data_dict
                return None
                    
        except socket.timeout:
            is_connected_to_ap = False
            CyInterface().addImmediateMessage("AP Error: Connection timed out.", "")
            return None
            
        except socket.error, e:
            err_code = e[0]
            
            if err_code == errno.ECONNREFUSED:
                is_connected_to_ap = False
                CyInterface().addImmediateMessage("AP Error: Connection refused. Is the client open?", "")
                return None
                
            if err_code in (errno.EWOULDBLOCK, errno.EAGAIN, 10035):
                return None
                
            is_connected_to_ap = False
            CyInterface().addImmediateMessage("AP Network Error Code: " + str(err_code), "")
            return None
            
    finally:
        # This finally block is now legal because it only pairs with the outer try
        try:
            socket_to_archipelago.close()
        except Exception:
            pass

def initialConnectToArchipelago():
    if not hasConnectedToArchipelago:
        showPopup("Set Up Archipelago Connection Settings", "Go into the BUG Options (Alt+Ctrl+O) and enter in your connection information.")
    else:
        server = BugOptions.getOption("Archipelago__ArchipelagoServer").getValue()
        username = BugOptions.getOption("Archipelago__ArchipelagoUsername").getValue()
        password = BugOptions.getOption("Archipelago__ArchipelagoPassword").getValue()
        connectToArchipelagoServer(server, username, password)
        if not isConnectedToArchipelago:
            showPopup("Set Up Archipelago Connection Settings", "Go into the BUG Options (Alt+Ctrl+O) and enter in your connection information.")


def connectToArchipelagoServer(server, username, password):
    if server == "":
        showPopup("Connection Error", "Please enter a server name.")
        return
    if username == "":
        showPopup("Connection Error", "Please enter a slot name.")
        return
    # TODO Should check if all fields have any characters that will cause parsing errors
    # This maybe shouldn't be necessary once the BUG options screen works right
    BugOptions.getOption("Archipelago__ArchipelagoServer").setValue(server)
    BugOptions.getOption("Archipelago__ArchipelagoUsername").setValue(username)
    BugOptions.getOption("Archipelago__ArchipelagoPassword").setValue(password)

    messageDict = { "type":"Connect", "server":server, "username":username, "password":password }
    dataDict = sendAndReceiveData(messageDict)
    CyInterface().addImmediateMessage(str(dataDict), "")

    if dataDict is None:
        showPopup("Connection Error", "No packet received from connectToArchipelagoServer")
    elif dataDict.get("cmd") == "Connected":
        showPopup("Connected", "Successfully Connected")
    else:
        showPopup("Connection Error", "Unexpected packet type: " + dataDict.get("cmd") + " in connectToArchipelagoServer")
    
            
