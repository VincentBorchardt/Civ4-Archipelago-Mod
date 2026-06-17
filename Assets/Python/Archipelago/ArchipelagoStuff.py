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

    # Not sure what error to try and catch for "connection refused"--it's "10061" on Windows 11
    socket_to_archipelago = socket.socket()  # instantiate
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number
    socket_to_archipelago.connect((host, port))  # connect to the server
    socket_to_archipelago.sendall(messagePickle)  # send message

    if waitForRead:
        try:
            data_pickle = socket_to_archipelago.recv(1024)  # receive response
            if data_pickle:
                data_dict = pickle.loads(data_pickle)
                if "cmd" in data_dict:
                    return data_dict
            # TODO throw a good error message
            return None
                
        except socket.error, e:
            # TODO I want this to always be None; I guess returning nothing does that, but need a cleaner thing (especially if I add a timeout)
            err_code = e[0]
            # If the code is just "no data available right now", release control
            if err_code in (errno.EWOULDBLOCK, errno.EAGAIN, 10035):
                return None

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
    
            


			
	

