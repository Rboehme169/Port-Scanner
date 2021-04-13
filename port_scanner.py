## Port Scanner 

import socket
import subprocess
import sys
from datetime import datetime
import ipaddress

#subprocess.call(clear, shell=True)

def portScan(): #Add Menu to choose your computer or a different computer.
    while True:
        #def targetSelect()
        print("Would you like to scan this computer or a different computer?\n\nSelect an option then press ENTER\n\n1. This Computer\n2. Another Computer")
        compChoice = int(input())
        if compChoice == 1:
           targetName = socket.gethostname()
           targetIP = socket.gethostbyname(targetName)
           print("Scanning ", targetName)
           #return targetIP
        elif compChoice == 2:
            targetName = input("Enter the name of the computer you would like to scan: ") ##Maybe change this to an if else for IP address or hostname flt vs str
            targetIP = socket.gethostbyname(targetName)
            #return targetIP
        else:
            print("You are a nerd. Try again.\n")
            portScan()
            #targetSelect() unless there is a way to just make the reinput

        #def scanFoo():
        print("-" * 60)
        print("Scanning remote host", targetIP)
        print("-" * 60)
    
        startTime = datetime.now()
    
        try:
            for port in range(1,1025):
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((targetIP, port))
                if result == 0:
                    print("Port {}:     Open".format(port)) #no longer broken, still looks like shit.
                sock.close()  #Should I include an option to scan a different computer and have it return? Probably
        
        except KeyboardInterrupt:
            print("You have chosen to close the program.")
            sys.exit()
    
        except socket.gaierror:
            print("Could not find computer. Try again.") #I want this to return to input instead
            portScan()
    
        except socket.error:
            print("Unable to connect. Try again") #again, want this to return to start
            portScan()
    
        endTime = datetime.now()
    
        timeElapsed = endTime - startTime
    
        print("Scanning Completed in: ",timeElapsed)
        
        #portScan()
    
portScan()


