# osrc.py

# osrc.py is the core of the Open Source Reef Controller program. All the good stuff happens here.

import config
import timing
import gui

# ~~Initialization~~

# Creates a list of lighting objects of class Light
# Variables accessed by light_list[i].foo
for i in range(0,len(Lighting_Channels)):
	light_list.append(Light(Lighting_Channels[i]))

# ~~Main program loop~~
while True:	
	# Check lighting timers
	for i in range(0,len(light_list)):
		if intimewindow(light_list[i].ontime,light_list[i].offtime):
			light_list[i].powerstate = True
		else
			light_list[i].powerstate = False
			
	# Set GPIO states
	
	# GUI stuff