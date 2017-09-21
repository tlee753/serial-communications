"""
UART Python Sender
- Protocol: UART
- Device: Raspberry Pi
- Role: Sender
- Data: Ascii Characters
- Speed: Live

- @author Tyler Lee
- @version 1.0
"""

import serial

print("Program Running")

# initalization UART interface
serialConnection = serial.Serial("/dev/ttyAMA0")

if serialConnection.isOpen(): # ensure serial connection is ready
	print("Sending on UART connection...")
	while True: # runs in real time
		userInput = input("Transmit: ") # obtain user input
		serialConnection.write(userInput) # transmit

print("Program Ending")