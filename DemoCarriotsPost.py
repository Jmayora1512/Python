#!/usr/bin/python3
# -*- coding: utf-8 -*-
import http.client
import urllib.request
import urllib.parse
import json
import time

api_url = "http://api.carriots.com/streams"
device = "SensorLuz@jmayora.jmayora"  # Mi id_developer
api_key = "4f18e390209cb527dc671acf12f4bc6c770f5c8143c9ec0a3b61d6ffcff15aa0"  #Mi Carriots apikey

#Obtener el tiempo
timestamp = int(time.time())

#Parametros del cuerpo
params = {"protocol": "v2",
                "device": device,
                "at": timestamp,
                "data": dict(
                    temp=11,
                    hum =89)} 
binary_data = json.dumps(params).encode('ascii')

#Cabecera
header = {"User-Agent": "raspberrycarriots",
				"Content-Type": "application/json",
				"carriots.apikey": api_key}
				
#Requerimiento
req = urllib.request.Request(api_url,binary_data,header)
f = urllib.request.urlopen(req)

#Imprimir respuesta
#print(f.read().decode('utf-8'))

data=json.loads(f.read().decode('utf-8'))
print(json.dumps(data,indent=4,sort_keys=True))
