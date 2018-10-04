import Interfaces as interface
import Status as status
import Log as log
import Routing as routing

def Menu():
    print('Please select any option:\n 1.-Check interfaces.\n2.-Check router/switch status.\n3.-Check logs.\n4.-Check Routing Protocols.\n')
    option= int(input('>').strip(" "))
    if option == 1:
        MenuInterface()
    elif option == 2:
        MenuStatus()
    elif option == 3:
        MenuLogs()
    elif option == 4:
        MenuRouting()

def MenuInterface():
    print("We can do the following:\n1.-Check interfaces status(up/down/admin-down) with ip addressing.\n2.-Check interface statistics.\n3.-Check Interface configurations.\n")
    option= int(input('>').strip(" "))
    if option == 1:
        interface.status(connection)
    elif option == 2:
        interface.statistics(connection)
    elif option == 3:
        interface.configs(connection)

def MenuStatus():
    print("We can do the following:\n1.-Check cpu status.\n2.-Check memory status.\n3.-Check inventory.\n4.-Check Version.\n")
    option= int(input('>').strip(" "))
    if option == 1:
        status.cpu(connection)
    elif option == 2:
        status.memory(connection)
    elif option == 3:
        status.inventory(connection)
    elif option == 4:
        status.version(connection)
    
    
def MenuLog():
    print("We can do the following:\n1.-Check entire log buffer.\n2.-Filter logs by KW.\n")
    option= int(input('>').strip(" "))
    if option == 1:
        log.buffer(connection)
    elif option == 2:
        log.keyword(connection)


def MenuRouting():
    print("We can do the following:\n1.-Check Routing configuration.\n2.-Check Eigrp.\n3.-Check OSPF.\n4.-Check BGP.\n")
    option= int(input('>').strip(" "))
    if option == 1:
        routing.config(connection)
    elif option == 2:
        routing.eigrp(connection)
    elif option == 3:
        routing.ospf(connection)
    elif option == 4:
        routing.bgp(connection)
        
