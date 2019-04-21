ABOUT:

	This program is designed to see if a specific device has come in range of an AP. It uses the output 
	from airodump-ng. For more information on what the data is look up the documentation for
	airodump-ng. 


REQUIREMENTS:

	1) Must have WiFi Adapter that is in monotor mode
	2) Must have Aircrack-ng installed
	3) Must know MAC address of the device you are looking for 
	4.a) For Laptops you must not be connected to a network to recieve Probe Requests. 
	4.b) For Phones you must have the WiFi on and connected to a network to recieve Probe Requests. 
	

PROCEDURE:

	1) Open ProbeMonitor.py 
	2) Replay the variable MAC with the MAC address you are tracking and save
	3) Open two terminals and make sure you are in SeniorResearch directory. 
		
		Terminal_1:$ sudo airodump-ng -w AiroDumpOutput --output-format csv wlan0
		Terminal_2:$ python DeviceStatus.py XX:XX:XX:XX:XX:XX

		Where XX:XX:XX:XX:XX:XX is the MAC address of the device you are monitoring 
	
	4) Execute Terminal_1 wait a few seconds then execute Terminal_2
	5) This program will run for 5 min. This is just a little longer than airodump-ng runs for

	TO RUN THE PROCEDURE AGAIN YOU MUST DELETE ALL THE FILES EXCEPT FOR DeviceStatus.py and README.md
	BEFORE REPEATING

OUTPUT:
	
	
	The output on the terminal will look like this:

		[Status: 0 Time Stamp: 2019-04-20 14:45:37.263072]
	
	Where Status is either 0 or 1. 
		If status is 1 that means that the device has connected to an AP. 
		If status is 0 that means that the device is not connected to an AP. 


	Once the program is finshed there will be a text file generated called "ClientStatus.txt" which
	will have all the outputs from the terminal.