ABOUT:

	This program is meant to test wifi probe tracking for a single device. It uses the output 
	from airodump-ng. For more information on what the data is look up the documentation for
	airodump-ng  


REQUIREMENTS:

	1) Must have WiFi Adapter that is in monotor mode
	2) Must have Aircrack-ng installed
	2) Must know MAC address of the device you are looking for 
	

PROCEDURE:

	1) Open ProbeMonitor.py 
	2) Replay the variable MAC with the MAC address you are tracking and save
	3) Open two terminals and make sure you are in SeniorResearch directory. 
		
		Terminal_1:$ sudo airodump-ng -w AiroDumpOutput --output-format csv wlan0
		Terminal_2:$ python ProbeMonitor.py
	
	4) Execute Terminal_1 wait a few seconds then execute Terminal_2
	5) This program will run for 5 min. This is as long as airodump-ng runs for as well

	TO RUN THE PROCEDURE AGAIN YOU MUST DELETE ALL THE FILES EXCEPT FOR ProbeMonitor.py and README.md
	BEFORE REPEATING

OUTPUT:
	
	
	The output will look like this:

		['XX:XX:XX:XX:XX:XX', ' 2019-04-20 00:04:05', ' 2019-04-20 00:04:05', ' -45', '        6', ' (not associated) ', 'someWifi']
	
	This is what it means:
		
		[Client_MAC, First Seen, Last Seen, Power, Frame, Probe]

	There is also a text file called "ClientDataFinal.txt" this contains all the data that was recieved from the device
	with that MAC address. 

DISCLAIMER:
	
	For Laptops you will pick up probes when it is on and the wifi is off. 
	For Phones you must have the WiFi on
