"""
Practical Internet of Things (loT) with RaspberryPi

MODULE 2: Practical exercise
	Make a python program that makes an LED blink three times when a button
	is pressed. There should be a delay of two seconds between blinkx.
	This exercise will be corrected by some of your partners.
	
	NOTE: 
		This program uses the pin 17 and 18 of BCM numering
			27(out): LED
			10(in) : Button
		It's possible to change the time bweteen blinks changing the
		variable blink_time. Tis time represents the time that is the
		LED ON and OFF. 
		Example: if blink_time = 2, the LED is 1s ON and 1s OFF.
"""

#library import
import RPi.GPIO as GPIO
import time

#set the GPIO modes to BCM numering
GPIO.setmode(GPIO.BCM)

#set LEDs pin (27) and button pin (18)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(10,GPIO.IN,pull_up_down=GPIO.PUD_UP)

#defining local variables
led_estate = False	#Initial state of LED. false = OFF
blink_time = 2

#loop that reads the button input
while True:
    input_state = GPIO.input(10)
    if not input_state :				#if the button is pressed
        for n in range(6):				#Do six times the code
            led_estate = not led_estate	# estatus = not status
            GPIO.output(27,led_estate)  # ON/OFF the LED dependig of the state
            time.sleep(blink_time/2)	# wait the blink time
