#import Interfaces as interface
#import Status as status
#import Log as log
#import Routing as routing
import Connection as connect
import sys

def Menu():
    print('Please select any option:\n1.-Check interfaces.\n2.-Check router/switch status.\n3.-Check logs.\n4.-Check Routing Protocols.\n')
    print("You can type 99 too if you want to close this script.\n")
    option= int(input('>').strip(" "))
    if option == 1:
        MenuInterface()
    elif option == 2:
        MenuStatus()
    elif option == 3:
        MenuLog()
    elif option == 4:
        MenuRouting()
    elif option == 99:
        sys.exit()

def MenuInterface():
    print("We can do the following:\n1.-Check interfaces status(up/down/admin-down) with ip addressing.\n2.-Check interface statistics.\n3.-Check Interface configurations.\n4.-Go back.\n")
    print("You can type 99 too if you want to close this script.\n")
    option= int(input('>').strip(" "))
    if option == 1:
        interface.status(connection)
    elif option == 2:
        interface.statistics(connection)
    elif option == 3:
        interface.configs(connection)
    elif option == 4:
        Menu()
    elif option == 99:
        sys.exit()

def MenuStatus():
    print("We can do the following:\n1.-Check cpu status.\n2.-Check memory status.\n3.-Check inventory.\n4.-Check Version.\n5.-Go back\n")
    print("You can type 99 too if you want to close this script.\n")
    option= int(input('>').strip(" "))
    if option == 1:
        status.cpu(connection)
    elif option == 2:
        status.memory(connection)
    elif option == 3:
        status.inventory(connection)
    elif option == 4:
        status.version(connection)
    elif option == 5:
        Menu()
    elif option == 99:
        sys.exit()    
    
def MenuLog():
    print("We can do the following:\n1.-Check entire log buffer.\n2.-Filter logs by KW.\n3.-Go Back.\n")
    print("You can type 99 too if you want to close this script.\n")
    option= int(input('>').strip(" "))
    if option == 1:
        log.buffer(connection)
    elif option == 2:
        log.keyword(connection)
    elif option == 3:
        Menu()
    elif option == 99:
        sys.exit()

def MenuRouting():
    print("We can do the following:\n1.-Check Routing configuration.\n2.-Check Eigrp.\n3.-Check OSPF.\n4.-Check BGP.\n5.-Go Back.\n")
    print("You can type 99 too if you want to close this script.\n")
    option= int(input('>').strip(" "))
    if option == 1:
        routing.config(connection)
    elif option == 2:
        routing.eigrp(connection)
    elif option == 3:
        routing.ospf(connection)
    elif option == 4:
        routing.bgp(connection)
    elif option == 5:
        Menu()
    elif option == 99:
        sys.exit()
        
print("Please add the following information in order to create a telnet connection to your Router/Switch:")
host = input("Please add the ip address of your router:").strip(" ")
username = input("Please add the username if needed (if not just type None):").strip(" ")
password = input("Please add the password if needed (if not just type None):").strip(" ")
enablepwd = input("Please add the enable password if needed (if not just type None):").strip(" ")
port = input("Please add the port if needed (if not just type None):").strip(" ")

if username == 'None' or username == 'none' :
    username = None

if password == 'None' or password == 'none' :
    password = None
    
if enablepwd == 'None' or enablepwd == 'none' :
    enablepwd = None
    
if port == 'None' or port == 'none' :
    port = None

connection = connect.connection(host, username, password, enablepwd, port)
Menu()
