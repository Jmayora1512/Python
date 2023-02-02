#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(22, GPIO.OUT)

loop_count = 0

def morsecode ():

	#Punto punto punto
	GPIO.output(22,GPIO.HIGH)
	time.sleep(.1)
	GPIO.output(22,GPIO.LOW)
        time.sleep(.1)
        GPIO.output(22,GPIO.HIGH)
        time.sleep(.1)
        GPIO.output(22,GPIO.LOW)
        time.sleep(.1)
        GPIO.output(22,GPIO.HIGH)
        time.sleep(.1)

        #Dash Dash Dah
        GPIO.output(22,GPIO.LOW)
        time.sleep(.2)
        GPIO.output(22,GPIO.HIGH)
        time.sleep(.2)
        GPIO.output(22,GPIO.LOW)
        time.sleep(.2)
        GPIO.output(22,GPIO.HIGH)
        time.sleep(.2)
        GPIO.output(22,GPIO.LOW)
        time.sleep(.2)
        GPIO.output(22,GPIO.HIGH)
        time.sleep(.2)
        GPIO.output(22,GPIO.LOW)
        time.sleep(.2)

        #Punto punto punto
        GPIO.output(22,GPIO.HIGH)
        time.sleep(.1)
        GPIO.output(22,GPIO.LOW)
        time.sleep(.1)
        GPIO.output(22,GPIO.HIGH)
        time.sleep(.1)
        GPIO.output(22,GPIO.LOW)
        time.sleep(.1)
        GPIO.output(22,GPIO.HIGH)
        time.sleep(.1)
        GPIO.output(22,GPIO.LOW)
        time.sleep(.1)

os.system('clear')
print ("Morse code")
loop_count = input ("¿Cuántas veces le gustaría mensaje SOS ? ?: ")
while loop_count > 0:
	loop_count = loop_count - 1
	morsecode ()	
