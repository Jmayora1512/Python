#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(10, GPIO.IN)

print ("------------------")
print ("Button + GPIO")
print ("------------------")

print (GPIO.input(10))
while True:
    if (GPIO.input(10) == False):
        print("Boton presionado")
        os.system('date')
        print (GPIO.input(10))
        time.sleep(3)
        for n in range (1, 4):
            GPIO.setup(17,GPIO.OUT)
            #Turn LEDs on
            GPIO.output(17,GPIO.HIGH)
            time.sleep(2)
            #Turn LEDs off
            GPIO.output(17,GPIO.LOW)
            time.sleep(1)
        break
    else:
        os.system('clear')
        print ("Estamos esperando que presiones el boton")
time.sleep(1)
