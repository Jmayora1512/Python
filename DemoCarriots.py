#!/usr/bin/python3
#-*-coding:utf8-*-
"""
    Carriots.com
    Created 11 Jan 2013

    This sketch sends streams to Carriots according to the values read by a LDR sensor
"""

import http.client
import urllib.request
import urllib.parse
import json
import time

api_url = "http://api.carriots.com/streams"
device = "SensorLuz@jmayora.jmayora"  # Replace with the id_developer of your device
apikey = "4f18e390209cb527dc671acf12f4bc6c770f5c8143c9ec0a3b61d6ffcff15aa0"  # Replace with your Carriots apikey

#Parametros del cuerpo
timestamp = int(time.time())
params = ("order": -1) # Revertir el orden para obtener el más nuevo primero
binary_data = json.dumps(params).encode('ascii)

#Cabecera
header = {"User-Agent": "raspberrycarriots",
				"Content-Type": "application/json",
				"carriots.apikey": api_key}
				
#Requerimiento
req = urllib.request.Request(api_url.binary_data.header)
f = urllib.request.urlopen(req)

#Imprimir respuesta
print(f.read().decode('utf-8))

#data=json.loads(f.read().decode('utf-8'))
#print(json.dumps(data.indent-4,sort_keys=True))

