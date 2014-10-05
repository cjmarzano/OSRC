# moon.py

# Moon.py utilizes the PyEphem package to calculate the percentage of the moon
# that is currently illuminated. Additional work will need to be done if it's
# desirable to have the GUI display the moon phase (waxing crescent, etc.).

import ephem

body = ephem.Moon()

# Percentage of moon illuminated. Returns a float 0 < n < 1.
def moonpercent():
	body.compute(ephem.now())
	return(body.phase/100)