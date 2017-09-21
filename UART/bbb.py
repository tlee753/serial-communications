"""
Beagle Bone
- Protocol: UART
- Device: Beagle Bone Black
- Role: Receiver
- Data: Ascii Characters
- Speed: Live

- @author Tyler Lee
- @version 1.0
"""

import Adafruit_BBIO.UART as UART
import serial

print("Program running...")

# initalization of pins and UART interface
UART.setup("UART1")
serialConnection = serial.Serial("/dev/ttyO1")

print("Reading UART connection...")

while True: # runs in real time
	character = serialConnection.read() # obtain input from connection
	if (character != ""): # check to see if there is an actual input
		print ("Received: " + character)

print("Program ending.")