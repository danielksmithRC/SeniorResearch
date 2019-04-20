import csv
import time
import subprocess
import sys


MAC = '38:DE:AD:DB:BA:64'
cmd = "sudo airodump-ng -w Research/AiroDumpOutput --output-format csv wlan0"

def deciferClientFile():
    with open('ClientData.csv') as fileRead:
        reader = csv.reader(fileRead)
        
        for row in reader:
            if row:
                if row[0] == MAC:
                    print row
                    file.write(str(row) + "\n")
                    #clientData.append(str(row))
                    

        
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

    while True:
        makeClientFile()
        deciferClientFile()
        #for x in clientData:
            #print(x)
            #file.write(x)
        time.sleep(3)


file = open('ClientFinalData.txt', 'w')
#clientData = []
#subprocess.run(cmd, shell=True)
#time.sleep(3)
mainLoop()
