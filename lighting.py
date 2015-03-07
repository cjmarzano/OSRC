# lighting.py

# Lighting.py controls all calculations pertaining to light intensity and duration.

# The light class allows dynamic creation of new lighting objects as defined in config.py.
class Light:
	def __init__(self, input_array):
		self.color = input_array[0]
		self.location = input_array[1]
		self.pwmable = input_array[2]	# User defined True/false variable for PWM capability (LED)
		self.ontime = input_array[3]
		self.offtime = input_array[4]
		self.pwmcycle = 0				# PWM duty cycle 0-100
		self.powerstate = False			# Power state (on/off)