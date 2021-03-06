
import RPI.GPIO as GPIO	
import time
import os

CLK = 18
MISO = 23
MOSI = 24
CS = 25

def setupSpiPins(clkPin, misoPin, mosiPin, csPin):
    ''' Set all pins as an output except MISO (Master Input, Slave Output)'''
    pass

def readAdc(channel, clkPin, misoPin, mosiPin, csPin):
    if (channel < 0) or (channel > 7):
        print "Invalid ADC Channel number, must be between [0,7]"
        return -1
        
    # Datasheet says chip select must be pulled high between conversions

    
    # Start the read with both clock and chip select low

    
    # read command is:
    # start bit = 1
    # single-ended comparison = 1 (vs. pseudo-differential)
    # channel num bit 2
    # channel num bit 1
    # channel num bit 0 (LSB)
    read_command = 0x18
    read_command |= channel
    
    sendBits(read_command, 5, clkPin, mosiPin)
    
    adcValue = recvBits(12, clkPin, misoPin)
    
    # Set chip select high to end the read


  
    return adcValue
    
def sendBits(data, numBits, clkPin, mosiPin):
    ''' Sends 1 Byte or less of data'''
    
    data <<= (8 - numBits)
    
    for bit in range(numBits):
    pass
        # Set RPi's output pin high or low depending on highest bit of data field
        
        # Advance data to the next bit
        
        # Pulse the clock pin HIGH then immediately low


def recvBits(numBits, clkPin, misoPin):
    '''Receives arbitrary number of bits'''
    retVal = 0
    
    # For each bit to receive
        # Pulse clock pin high then immediately low
        
        # Read 1 data bit in and include in retVal
        
        # Advance input to next bit
    
    # Divide by two to drop the NULL bit
    return (retVal/2)
    
    
if __name__ == '__main__':
    try:
        GPIO.setmode(GPIO.BCM)
        setupSpiPins(CLK, MISO, MOSI, CS)
    
        while True:
            val = readAdc(0, CLK, MISO, MOSI, CS)
            print "ADC Result: ", str(val)
            time.sleep(5)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit(0)

