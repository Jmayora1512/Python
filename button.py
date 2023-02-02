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
        time.sleep(5)
        for n in range (1, 3):
            print(n)
        break
    else:
        os.system('clear')
        print ("Estamos esperando que presiones el boton")
time.sleep(1)
