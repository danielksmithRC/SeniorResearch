ABOUT: 


	Here are two programs that can be used to research Probe Requests on a specific device
	Both folders contain the program along with a README for that program. There is also
	a Data Folder that you can put data findings of your own into. 


PROCEDURE/PREREQUISITES:

	1.  Purchase a Raspberry Pi 3 and a TP-WN722N V2 or V3 that supportsmonitor mode
	2.  Download Raspbian here1and use balenaEtcher2to put the OS onto themicroSD card
	3.  Insert  microSD  card  into  Raspberry  Pi  and  make  sure  the  keyboard,mouse, and monitor are plugged into your Raspberry Pi before pluggingin the power cord
	4.  After finishing initial setup open the terminal and executesudo apt-getupdate
	5.  If you executesudo iw devwhile your TP-WN722N is connected to yourRaspberry Pi you will notice that only wlan1 (which is the wifi chipsetof the Pi) is visable.  To allow for the TP-WN722 to show up you mustinstall Re4son kernel.
	6.  Proceed to Re4son kernel3and follow the Manual Installation For Old Stable
	7.  Once Re4son kernel is installed you can executesudo iw devagain andsee that wlan0 is now visable.  Notice though that type for wlan0 is man-aged.  We need to enable monitor mode.
	8.  To enable monitor mode execute the following in the terminal:
		(a)sudo ip link set wlan0 down
		(b)sudo iw wlan0 set monitor control
		(c)sudo ip link set wlan0 up
		(d)sudo iw dev
	    Notice that type is now monitor for wlan0.
	9.  To get any data from wlan0 that is now in monitor mode we need to useairodump-ng  which  is  part  of  aircrack-ng  which  you  can  downloand  by executing sudo apt-get install aircrack-ng
	10. Now you can run sudo airodump-ng wlan0 to get the data that is coming into your TP-WN722N on monitor mode.
	11  You can now use these two programs.
	