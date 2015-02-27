# moon.py

# Moon.py utilizes the PyEphem package to calculate the percentage of the moon
# that is currently illuminated.

import ephem

body = ephem.Moon()

# Percentage of moon illuminated. Returns a float 0 < n < 1.
def moonpercent():
	body.compute(ephem.now())
	return(body.phase/100)