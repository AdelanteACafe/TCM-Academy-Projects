#!/bin/python

import sys
import socket
from datetime import datetime

#Define the Target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hotname to ipv4, allowing a hostname to be searched instead of/in addition to an ip address

else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

#Add a pretty banner
print("-" * 50)#actual banner
print("Acquiring Target "+target)
print("Time Started: "+str(datetime.now()))
print("-" * 50)#again, the actual banner

#The following is basically one big loop
try: 
	for port in range(50,85):#the ports to be scanned
					#af_inet is ipv4
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1) #one second waiting to connect
		result = s.connect_ex((target,port)) #returns an error indicator
		if result == 0:
			print("The port () is open".format(port))
		s.close() #this closes the connection

#The following are exceptions to the above loop

except KeyboardInterrupt: #like "control C"
	print("\nExiting program.")
	sys.exit()#allows for a clean exit in such a case
	
except socket.gaierror:
	print("Hostname could not be resolved, sorry dude.")
	
except socket.error:
	print("Sorry. Couldn't connect to server.")
	sys.exit()# Again, exits prograam
	

