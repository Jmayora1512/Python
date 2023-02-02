#!/usr/bin/python3
# -*- coding: utf-8 -*-
import http.client
import urllib.request
import urllib.parse
import json
import time

api_url = "http://api.carriots.com/streams/9cbfc5128a865377595ce942d28e3689eb76d9e37e474e17c897d1d2eae51692@jmayora.jmayora/"
#device = "SensorLuz@jmayora.jmayora"  # Replace with the id_developer of your device
api_key = "4f18e390209cb527dc671acf12f4bc6c770f5c8143c9ec0a3b61d6ffcff15aa0"  # Replace with your Carriots apikey

#Parametros del cuerpo
timestamp = int(time.time())
params = {} 
binary_data = json.dumps(params).encode('ascii')

#Cabecera
header = {"carriots.apikey": api_key}
				
#Requerimiento
req = urllib.request.Request(api_url,binary_data,header)
req.get_method = lambda: "DELETE"
f = urllib.request.urlopen(req)

#Imprimir respuesta
#print(f.read().decode('utf-8'))

data=json.loads(f.read().decode('utf-8'))
print(json.dumps(data,indent=4,sort_keys=True))
