import csv
import time
import subprocess
import sys
import datetime
#from datetime import datetime


MAC = 'XX:XX:XX:XX:XX:XX'
EndProgram = time.time() + 60 * 5


#PRE: Must have a file called 'ClientData.csv' that has only the bottom portion
#      of the airodump-ng output
#POST: This will will for the client with the MAC address defined in the variable
#        MAC. If that device is there it will append  1 and a time stamp otherwise
#        it will append 0 and a time stamp to clientData
def deciferClientFile(currDateTime):
    with open('ClientData.csv') as fileRead:
        reader = csv.reader(fileRead)

        DeviceStatus = 0
        BSSID = ""
        
        for row in reader:
            if row:
                if row[0] == MAC:
                    lastSeenString = row[2]
                    lastSeen = datetime.datetime.strptime(lastSeenString, " %Y-%m-%d %H:%M:%S")
                    
                    if lastSeen > currDateTime: 
                        DeviceStatus = 1
                        BSSID = str(row[5])

        print("Status: " + str(DeviceStatus) + " Time Stamp: " + str(datetime.datetime.now()))
        clientStatus.append("Status: " + str(DeviceStatus) + " Time Stamp: " + str(datetime.datetime.now()) ) 
                    
        fileRead.close()
        
                
#PRE: Must have made a file called "AiroDumpOutput-01.csv with airodump-ng
#POST: This write to 'ClientData.csv' the bottom protion of airodump-ng which
#        containts information about clients around the TP-WN722N 
def makeClientFile():
    
    with open('AiroDumpOutput-01.csv') as fileRead:
        reader = csv.reader(fileRead)
        with open('ClientData.csv', 'w') as fileWrite:
        
            writer = csv.writer(fileWrite)

            outputfile = open('ClientData.csv','w')

            count = 0

            for line in reader:
                if not line:
                    count += 1

                if count > 1:
                    writer.writerow(line)

            fileWrite.close()
        fileRead.close()
    

def mainLoop():

    delay = 5

    while time.time() < EndProgram:

        currDateTime = datetime.datetime.now() - datetime.timedelta(seconds=delay)
        
        #print("currDateTime Before: " + str(currDateDummpy))
        #This will allow for 'AiroDumpOutput-01.csv to update
        time.sleep(delay)
        makeClientFile()
        deciferClientFile(currDateTime)
        

    #Once the program is finished we want to write this data to
    # "ClientFinalData.txt
    file = open("ClientStatus.txt", "w")
    
    for row in clientStatus:
        file.write(row + "\n")

    file.close()

clientStatus = []
mainLoop()
 
