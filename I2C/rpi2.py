import smbus
import time

bus = smbus.SMBus(1) # instantiate bus
slaveAddress = 0x04 # assign a slave address

def writeNumber(value): # function to write value
    bus.write_byte(slaveAddress, value)

def readNumber(): # function to read value
    number = bus.read_byte(slaveAddress)
    return number

while True: # continuous loop
    var = input(“Enter 1 – 9: “) # get user value to write
    if not var: # quick error check
        continue

    writeNumber(var) # write value
    print “RPI: Hi Arduino, I sent you “, var
    time.sleep(1) # wait one second

    number = readNumber() # read value
    print “Arduino: Hey RPI, I received a digit “, number
    print # spacing