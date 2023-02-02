#!/usr/bin/env python
import os
import datetime
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

DEBUG = 1
GPIO.setmode(GPIO.BCM)

def RCtime (RCpin): #Esta funcion esta disenada para configurar los pines GPIO.
	reading = 0
        #Cofigura los pines como salida y en estado bajo.
	GPIO.setup(RCpin, GPIO.OUT)
	GPIO.output(RCpin, GPIO.LOW)
 
 	time.sleep(.1)

 	GPIO.setup(RCpin, GPIO.IN)

	# Esto lleva alrededor de 1 milisegundo por ciclo de ciclo
	while (GPIO.input(RCpin) == GPIO.LOW):
        #Configure el bucle para tomar la lectura del pin LDR.                
		reading += 1
	return reading

while True:
	GetDateTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        #Use el comando datetime para registrar la fecha y hora actuales en una variable.
	LDRReading = RCtime(3) #Este comando llama a la funcion que creamos antes.
        print (RCtime(3)) #Imprime los resultados en la pantalla
	# Open a file
	fo = open("/home/pi/Desktop/Python/foo.txt", "wb")
	#Abra el archivo de texto y escriba el contenido en una memoria.
	fo.write (GetDateTime)
	#Escribe en el archivo la fecha y la hora actual.
	LDRReading = str(LDRReading)
	fo.write ("\n")
	fo.write (LDRReading)

	# Cierra el archivo.

	fo.close
	time.sleep(1)		

