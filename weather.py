#!/usr/bin/python3
import http.client
import urllib.request
import urllib.parse
api_url = "http://api.openweathermap.org/data/2.5/weather?"
api_key = "fb4194e7e12688fd791c52973742f113"
#idcity = "3117735"
idcity = "3646738"
req = urllib.request.Request(api_url+"id="+idcity+"&appid="+api_key)
f = urllib.request.urlopen(req)
print(f.read().decode('utf-8'))
#geonames
