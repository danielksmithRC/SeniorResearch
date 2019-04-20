import csv
import time
import subprocess
import sys


MAC = 'XX:XX:XX:XX:XX:XX'
EndProgram = time.time() + 60 * 5


#PRE: Must have a file called 'ClientData.csv' that has only the bottom portion
#      of the airodump-ng output
#POST: This will find the client with the MAC address defined in the variable MAC
#         it will then append that information to an array called clientData
def deciferClientFile():
    with open('ClientData.csv') as fileRead:
        reader = csv.reader(fileRead)
        
        
        for row in reader:
            if row:
                if row[0] == MAC:
                    print row
                    clientData.append(str(row))                    
                    
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

    

    while time.time() < EndProgram:
        
        makeClientFile()
        deciferClientFile()
        #This will allow for 'AiroDumpOutput-01.csv to update
        time.sleep(3)

    #Once the program is finished we want to write this data to
    # "ClientFinalData.txt
    file = open("ClientFinalData.txt", "w")
    
    for row in clientData:
        file.write(row + "\n")

    file.close()

clientData = []
mainLoop()
 
