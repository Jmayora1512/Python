#!/usr/bin/python
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
#Turn LEDs on
GPIO.output(17,GPIO.HIGH)
time.sleep(1)
#Turn LEDs off
GPIO.output(17,GPIO.LOW)

GPIO.setup(18,GPIO.OUT)
#Turn LEDs on
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
#Turn LEDs off
GPIO.output(18,GPIO.LOW)

GPIO.setup(27,GPIO.OUT)
#Turn LEDs on
GPIO.output(27,GPIO.HIGH)
time.sleep(1)
#Turn LEDs off
GPIO.output(27,GPIO.LOW)

GPIO.setup(22,GPIO.OUT)
#Turn LEDs on
GPIO.output(22,GPIO.HIGH)
time.sleep(1)
#Turn LEDs off
GPIO.output(22,GPIO.LOW)

GPIO.setup(23,GPIO.OUT)
#Turn LEDs on
GPIO.output(23,GPIO.HIGH)
time.sleep(1)
#Turn LEDs off
GPIO.output(23,GPIO.LOW)

GPIO.setup(24,GPIO.OUT)
#Turn LEDs on
GPIO.output(24,GPIO.HIGH)
time.sleep(1)
#Turn LEDs off
GPIO.output(24,GPIO.LOW)

GPIO.setup(25,GPIO.OUT)
#Turn LEDs on
GPIO.output(25,GPIO.HIGH)
time.sleep(1)
#Turn LEDs off
GPIO.output(25,GPIO.LOW)

GPIO.setup(4,GPIO.OUT)
#Turn LEDs on
GPIO.output(4,GPIO.HIGH)
time.sleep(1)
#Turn LEDs off
GPIO.output(4,GPIO.LOW)

