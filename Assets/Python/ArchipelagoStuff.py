from CvPythonExtensions import *
from PyHelpers import *
from Popup import PyPopup

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
#lock = threading.Lock()

def showPopup(header, body):
	modPopup = PyPopup()
	modPopup.setHeaderString(header)
	modPopup.setBodyString(body)
	modPopup.launch()

def checkIfArchipelagoTech(tech):
	
	tech_info = gc.getTechInfo(tech)
    
	# FLAVOR_ARCHIPELAGO is FlavorValue(8); currently hardcoded
	flavor_weight = tech_info.getFlavorValue(8)
        if flavor_weight > 0:
                showPopup("This is an Archipelago Tech", popupMessage)

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

def isSocketConnected():
    try:
        socket_to_archipelago.getpeername()
    except socket.error:
        return False
    try:
        # this will try to read bytes  without removing them from buffer (peek only) (Windows doesn't have MSG_DONTWAIT)
        data = socket_to_archipelago.recv(16, socket.MSG_PEEK)
        if len(data) == 0:
            return False
    except OSError, e:
        if e.errno == errno.EWOULDBLOCK:
            return True  # socket is open and reading from it would block
        if e.errno == errno.ECONNREFUSED:
            return False  # socket was closed for some other reason
        else:
            showPopup("Unknown OSError", str(e.errno))
            return False
    except Exception, e:
        showPopup("Unknown Error", str(e))
        return False
    return True

def connectToArchipelagoServer(server, username, password):
    #if isSocketConnected():
    #showPopup("Connection Error", "Already connected to a server.")
    #return
    if server == "":
        showPopup("Connection Error", "Please enter a server name.")
        return
    if username == "":
        showPopup("Connection Error", "Please enter a slot name.")
        return
    #try: # Not sure what error to try and catch for "connection refused"--it's "10061" on Windows 11
    socket_to_archipelago = socket.socket()  # instantiate
    #socket_to_archipelago.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # enable address reuse
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    socket_to_archipelago.connect((host, port))  # connect to the server

    # THIS BREAKS IF YOU USE A ; IN THE FIELDS!!!
    #message = server + ";" + username + ';' + password
    messageDict = { "type":"connect", "server":server, "username":username, "password":password }
    messagePickle = pickle.dumps(messageDict, 2)
    #header = struct.pack('>I', len(serialized_data))

    socket_to_archipelago.sendall(messagePickle)  # send message
    
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
    
            


			
	

