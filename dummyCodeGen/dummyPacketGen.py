# This program should output packets containing x, y values for the tracked puck 
#	as well as a time stamp in milliseconds for when the packet was sent.
#	seconds begin at 0 when program begins.


# User should input a time interval (>167) for how long between packets to be sent output
#	167 is the time in ms between frames on a 60fps camera so the sample rate for packets
#	should be at least greater than the time for each frame to be captured

import fileinput
import time
import constants
#import serial


accelY = 15.0
accelX = 10.0
xVal = -50
yVal = 10
tick = 0
tStamp=0


def getNewPacket(xVal, yVal, accelX, accelY):
	x = xVal
	y = yVal
	aX = accelX
	aY = accelY
	#print timeVal
	if (xVal + aX > 50 or xVal + accelX < -50): # X value would be beyound the table edges
		print "\t\t***** GOAL HERE *****\n"
		aX = -aX	#bouncing from wall calculation can go here			@@@@@
		x = xVal +  aX
	else:
		x = xVal +  aX

	if (yVal + aY > 50 or yVal + aY < 0): # Y value would be beyound the table edges
		aY = -aY	#bouncing from wall calculation can go here			@@@@@
		y = yVal +  aY
	
	else:
		y = yVal + aY


	packet = [xVal, yVal, tick]
	return x, y, aX, aY


def sendPacks(xVal, yVal, tick):#	function to be reworked for the correct communication method between programs	@@@@@@
	
	if(tick > 1000):
		print "\""+ str(xVal) + ":"+ str(yVal) + ":"+str(tick/1000.0) + "sec\"\n"

	else:
		print "\""+ str(xVal) + ":"+ str(yVal) + ":"+str(tick) + "ms\"\n"
		
#fin = open("")

td = raw_input("enter time interval in milliseconds: ")
tDelta = float(td)/1000
print "tDelta: " + str(tDelta) + " seconds\n"

fout = open("output.txt", "w")

#"""
i = 1
while(1):
	if(tick > int(td)*i):
		i += 1
		#sendPacks(xVal, yVal, tStamp)
		print >> fout, xVal, ":", yVal, ":", tStamp
		time.sleep(tDelta)
	
	xVal, yVal, accelX, accelY = getNewPacket(xVal, yVal, accelX, accelY);
	tick += constants.CAM_SPEED
	tStamp = tick
	print "\t\t\t\t#### TICK ", tick

#"""
