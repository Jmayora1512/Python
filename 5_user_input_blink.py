#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)

#Setup variables for user input
led_choice = 0
count = 0

os.system('clear')

print ("Which LED would you like to blink")
print ("1: Led 1")
print ("2: Led 2")
print ("3: Led 3")
print ("4: Led 4")
print ("5: Led 5")
print ("6: Led 6")
print ("7: Led 7")
print ("8: Led 8")

led_choice = input("Choose your option: ")

if ( led_choice == 1 ):
	os.system('clear')
	print "You picked the led 1"
	count = input("How many times would you like it to blink: ")
	while count > 0:
		GPIO.output(17,GPIO.HIGH)
		time.sleep(1)
		GPIO.output(17,GPIO.LOW)
		time.sleep(1)
		count = count - 1
   
if led_choice == 2:
        os.system('clear')
        print "You picked the led 2"
        count = input("How many times would you like it to blink: ")
        while count > 0:
                GPIO.output(18,GPIO.HIGH)
                time.sleep(1)
                GPIO.output(18,GPIO.LOW)
                time.sleep(1)
                count = count - 1

if led_choice == 3:
        os.system('clear')
        print "You picked the led 3"
        count = input("How many times would you like it to blink: ")
        while count > 0:
                GPIO.output(27,GPIO.HIGH)
                time.sleep(1)
                GPIO.output(27,GPIO.LOW)
                time.sleep(1)
                count = count - 1

if led_choice == 4:
        os.system('clear')
        print "You picked the led 4"
        count = input("How many times would you like it to blink: ")
        while count > 0:
                GPIO.output(22,GPIO.HIGH)
                time.sleep(1)
                GPIO.output(22,GPIO.LOW)
                time.sleep(1)
                count = count - 1

if led_choice == 5:
        os.system('clear')
        print "You picked the led 1"
        count = input("How many times would you like it to blink: ")
        while count > 0:
                GPIO.output(23,GPIO.HIGH)
                time.sleep(1)
                GPIO.output(23,GPIO.LOW)
                time.sleep(1)
                count = count - 1

if led_choice == 6:
        os.system('clear')
        print "You picked the led 1"
        count = input("How many times would you like it to blink: ")
        while count > 0:
                GPIO.output(24,GPIO.HIGH)
                time.sleep(1)
                GPIO.output(24,GPIO.LOW)
                time.sleep(1)
                count = count - 1

if led_choice == 7:
        os.system('clear')
        print "You picked the led 1"
        count = input("How many times would you like it to blink: ")
        while count > 0:
                GPIO.output(25,GPIO.HIGH)
                time.sleep(1)
                GPIO.output(25,GPIO.LOW)
                time.sleep(1)
                count = count - 1

if led_choice == 8:
        os.system('clear')
        print "You picked the led 8"
        count = input("How many times would you like it to blink: ")
        while count > 0:
                GPIO.output(4,GPIO.HIGH)
                time.sleep(1)
                GPIO.output(4,GPIO.LOW)
                time.sleep(1)
                count = count - 1

		

#print GPIO.input(10)
#while True:
#   if ( GPIO.input(10) == False ):
#     print ("Button Pressed")
#     os.system('date')
#     print GPIO.input(10)
#     time.sleep(5)
#   else:
#     os.system('clear')
#     print ("Waiting for you to press button")
#time.sleep(1)
 

