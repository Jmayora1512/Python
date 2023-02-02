#!/usr/bin/env python
import os
import datetime
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

DEBUG = 1
GPIO.setmode(GPIO.BCM)

def RCtime (RCpin):
#def RCtime (3):
	reading = 0
	GPIO.setup(RCpin, GPIO.OUT)
	GPIO.output(RCpin, GPIO.LOW)
        #GPIO.setup(3, GPIO.OUT)
        #GPIO.output(3, GPIO.LOW)
 
 	time.sleep(.1)

 	GPIO.setup(RCpin, GPIO.IN)
#	GPIO.setup(3, GPIO.IN)
	# This takes about 1 millisecond per loop cycle
	while (GPIO.input(RCpin) == GPIO.LOW):
#	while (GPIO.input(3) == GPIO.LOW):
		reading += 1
	return reading

while True:
	GetDateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	LDRReading = RCtime(3)
        print (RCtime(3))
	# Open a file
	fo = open("/home/pi/Desktop/Python/foo.txt", "wb")
	fo.write (GetDateTime)
	LDRReading = str(LDRReading)
	fo.write ("\n")
	fo.write (LDRReading)

	# Close opend file

	fo.close
	time.sleep(1)		

