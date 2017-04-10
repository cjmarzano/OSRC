# templogger.py
# 
# Developed by cmarzano
# 4/9/2017
#
# This script runs once to read a DS18B20 temperature sensor and report the result to Thingspeak.
# For regular measurements, it should be run multiple times through another script or scheduler, such as crontab.

import httplib, urllib
from w1thermsensor import W1ThermSensor
try:
	sensor = W1ThermSensor()
	temp = sensor.get_temperature(W1ThermSensor.DEGREES_F)
except RuntimeError:
	print('Failed to connect to sensor or read.')
	
# Input your thingspeak channel API key below
apikey = 'YOUR KEY HERE'

params = urllib.urlencode({'field1': temp, 'key':apikey})
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = httplib.HTTPConnection("api.thingspeak.com:80")
conn.request("POST", "/update", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
conn.close()
