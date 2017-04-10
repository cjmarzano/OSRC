# startup.py
# 
# Developed by cmarzano
# 4/9/2017

# Configuration
# Input your thingspeak channel API key below
apikey = 'YOUR KEY HERE'
	
# Report online status update to Thingspeak
import httplib, urllib
from time import gmtime, strftime

timestamp = strftime("%Y-%m-%d %H:%M:%S")
payload = ' OSRC online.'
payload = timestamp + payload

params = urllib.urlencode({'status':payload,'key':apikey})
headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
conn = httplib.HTTPConnection("api.thingspeak.com:80")
conn.request("POST", "/update", params, headers)
response = conn.getresponse()
print response.status, response.reason
data = response.read()
conn.close()
