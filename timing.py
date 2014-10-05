# timing.py

# Timing.py contains functions that pertain to the current time. Eventually
# it will be expanded to facilitate event scheduling.

import time

# Returns the formatted local time in 12hr HH:MM:SS AM/PM, most useful for GUI display
def formattedtime():
	return(time.strftime('%I:%M:%S %p'))

# Returns the current local time in 24hr HH:MM:SS, most useful for event scheduling
def currenttime():
	return(time.strftime('%H:%M:%S'))