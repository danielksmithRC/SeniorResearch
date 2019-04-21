import csv
import time
import subprocess
import sys
import datetime



#PRE:  Must have a file called 'ClientData.csv' that has only the bottom portion
#         of the airodump-ng output. This also takes in a variable called currDateTime
#         that is a datetime object. It must be delay seconds behind the current time
#POST: This will find the client with the MAC address defined in the variable MAC
#         it will then append that information to an array called clientData
def deciferClientFile(currDateTime):
    with open('ClientData.csv') as fileRead:
        reader = csv.reader(fileRead)
        
        
        for row in reader:
            if row:
                if row[0] == MAC:
                    print ("MAC: " + str(row[0]) + " Power: " + str(row[3]) + " TimeStamp: " + str(currDateTime))
                    clientData.append("MAC: " + str(row[0]) + " Power: " + str(row[3]) + " TimeStamp: " + str(currDateTime))                    
                    
        fileRead.close()
        
                
#PRE:  Must have made a file called "AiroDumpOutput-01.csv with airodump-ng
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
#        "ClientFinalData.txt
def mainLoop():

    # A delay of 5 seconds gives enough time to reach the TP-WN722N and still
    #   consider it as present.
    delay = 5

    while time.time() < EndProgram:

        # Must make a date time of now but push it back delay amount of seccond becuase
        # the program sleeps for that amount of time later on
        currDateTime = datetime.datetime.now() - datetime.timedelta(seconds=delay)
        makeClientFile()
        deciferClientFile(currDateTime)
        #This will allow for 'AiroDumpOutput-01.csv to update
        time.sleep(delay)

    #Now we write the clientData array to "ClientFinalData.txt
    file = open("ClientFinalData.txt", "w")
    
    for row in clientData:
        file.write(row + "\n")

    file.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Please enter the MAC address of the device you are monitoring."
    else:
        MAC = sys.argv[1]
        EndProgram = time.time() + 60 * 5
        clientData = []
        mainLoop()
 
