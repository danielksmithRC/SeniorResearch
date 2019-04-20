
import csv
import time
import subprocess
import sys


MAC = 'XX:XX:XX:XX:XX:XX'
EndProgram = time.time() + 60 * 5

def deciferClientFile():
    with open('ClientData.csv') as fileRead:
        reader = csv.reader(fileRead)
        
        
        for row in reader:
            if row:
                if row[0] == MAC:
                    print row
                    clientData.append(str(row))
                    
                    
                    

        fileRead.close()
        
                

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
        file = open("ClientFinalData.txt", "w")
        makeClientFile()
        deciferClientFile()

        for row in clientData:
            file.write(row + "\n")
            
        
        file.close()
        time.sleep(3)
        

clientData = []
mainLoop()
 
