import csv
import time
import subprocess
import sys
import datetime


#PRE: Must have a file called 'ClientData.csv' that has only the bottom portion
#      of the airodump-ng output. This also takes in a variable called currDateTime
#      that is a datetime object. It must be delay seconds behind the current time
#POST: This will look for the client with the MAC address defined in the variable
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
    

#PRE:  MAC and EndProgram must be set
#POST: This runs the main loop for the program. After the main loop of the
#        program is finished it writes the clientData array to a text file called
#        "ClientStatus.txt
def mainLoop():

    # A delay of 5 seconds gives enough time to reach the TP-WN722N and still
    #   consider it as present. 
    delay = 5

    while time.time() < EndProgram:

        currDateTime = datetime.datetime.now() - datetime.timedelta(seconds=delay)


        time.sleep(delay)
        makeClientFile()
        deciferClientFile(currDateTime)
        

    # Now clientStatus array needs to be written to "ClientStatus.txt" 
    file = open("ClientStatus.txt", "w")
    
    for row in clientStatus:
        file.write(row + "\n")

    file.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Please enter the MAC address of the device you are monitoring."
    else:
        MAC = sys.argv[1]
        EndProgram = time.time() + 60 * 5
        clientStatus = []
        mainLoop()
 
