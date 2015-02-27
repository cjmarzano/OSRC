# config.py

# Config.py is a centralized configuration file that contains a number of settings
# utilized throughout the controller.

import lighting
import moon

# ~~~~~~~~~~~~~~~~~~ GUI Configuration ~~~~~~~~~~~~~~~~~~
# Pixel size of display
screenwidth = 240
screenheight = 320

# ~~~~~~~~~~~~~~~~~~ Lighting Configuration ~~~~~~~~~~~~~~~~~~

# Lighting channels in format:
# ('Color', 'location', [PWM True or False, min PWM duty cycle, max PWM duty cycle], [ontime], [offtime])
Lighting_Channels = [('Blue', 'Display', [True, 30, 100], [12,00], [21,00]),
	('White', 'Display', [True, 30, 100], [12,00], [21,00]),
	('Red', 'Sump', [False], [20,00], [10,00])]
	
