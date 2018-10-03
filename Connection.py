from telnetlib import Telnet

def connection(*args):
    host = args[0]
    username = args[1]
    password = args[2]
    enablepwd = args[3]
    if(args[4] != None):
        port = args[4]
    else:
        port = 23
        
    tn = Telnet(host, port)

    if(tn.expect([b'>'],5)):
       tn.write(b"enable\n")
       if (tn.expect((b'Password'),5)):
           tn.write(enablepwd.encode('ascii') + b'\n')
    elif (tn.expect([b'#'],5)):
          print("Connection succeeded!!!")

    return(tn)

def closeconnetion(tn):    
    tn.close()
    
