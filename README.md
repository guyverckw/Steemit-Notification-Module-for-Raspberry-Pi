# Steemit-Notification-Module-for-Raspberry-Pi


Notification of your Steemit account activity on Raspberry Pi platform



Setup Procedure: (Draft)



Notification module setup procedures



Hardware setup:


1) Requirements:


	1x LCD Display with supported port expanders : PCF8574, the MCP23008 and the MCP23017 <-- for I2C connection


	1x LED (with resistor)




2) Wiring :
  

	i) LED:
  
  
  
		• Connect to GRD and GPIO 0 


	ii) LCD Display:
  
		Connect the pins on the right with the Raspberry Pi:

		• GND: Pin 6 (GND)

		• VCC: Pin 4 (5V)

		• SDA: Pin 3 (SDA)

		• SCL: Pin 5 (SCL)



3) Enable I2C interface:
	$ sudo raspi-config
	• Select "Interface Options"
	• Select "I2C"	
	• Select "Yes"
	• Select "OK"	
	• Select "Finish" to quit raspi-config

4) Check I2C address :

	$ sudo i2cdetect -y 1 



	Find the i2c address in the table displayed.


Software 
Setup:


1. Install Raspbian


2) Install LCD library -- RPLCD

 
	i) Install RPLCD directly from using pip:
 
 		
		$ sudo pip3 install RPLCD (for python2 use pip)

 
	ii) If you want to use I2C, you also need smbus:
      
		$ sudo apt-get install python3-smbus (for python2 use python-smbus)


3) Install Python-steem (piston-steem)
  
	$ sudo apt-get update
  
	$ sudo apt-get upgrade
  
	$ git clone https://github.com/xeroc/piston-lib/
  
	$ cd piston-lib
  
	$ python3 setup.py install --user


		
if get "fatal error: openssl/aes.h : No such file or directory" error, you may need to install Openssl Development package
  
	$ sudo apt-get install libssl-dev



4) Download Steem_notify.py


5) Change 'account_name' in line 10 of Steem_notify.py to your own Steemit account name

6) Update line 15 of Steem_notify.py to reflect your system's own i2c address
6) Run it!
  
	$ python3 Steem_notify.py
  
  
