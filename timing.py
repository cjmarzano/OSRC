# timing.py

# Timing.py contains functions that pertain to the current time. Eventually
# it will be expanded to facilitate event scheduling.

import time
import datetime

# Returns the formatted local time in 12hr HH:MM:SS AM/PM, most useful for GUI display
def formattedtime():
	return(time.strftime('%I:%M:%S %p'))

# Returns the current local time in 24hr HH:MM:SS, most useful for event scheduling
def currenttime():
	return(time.strftime('%H:%M:%S'))
	
# Returns true or false if the current time is between the on and off times.
# If the on time is greater than the off time, it is understood to be an overnight event.
# Input arguments should be ([24hr,min],[24hr,min])
def intimewindow(input_on_time, input_off_time):
	current_time = datetime.datetime.now().time()
	on_time = datetime.time(input_on_time[0],input_on_time[1])
	off_time = datetime.time(input_off_time[0],input_off_time[1])
	if on_time > off_time:
		if current_time > on_time or current_time < off_time:
			return(True)
	elif on_time < off_time:
		if current_time > on_time and current_time < off_time:
			return(True)
	elif current_time == on_time:
		return(True)
	return(False)