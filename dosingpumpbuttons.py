# dosingpumpbuttons.py
# 
# Developed by cmarzano
# 4/9/2017
#
# This script runs in the background to activate a dosing pump when a button is pressed.
# The primary purpose is to facilitate priming and manual control of the pumps when needed.
# This code is provided 'as is' without warranty of any kind, expressed or implied. Use at your own risk.

from time import sleep
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

# Connect to default Adafruit Motor Hat Address
try:
	mh = Adafruit_MotorHAT(addr=0x60)

# Create motor objects, initialize to known off state
	CalciumMotor = mh.getMotor(3)
	CalciumMotor.run(Adafruit_MotorHAT.FORWARD)
	CalciumMotor.run(Adafruit_MotorHAT.RELEASE)
	AlkalinityMotor = mh.getMotor(4)
	AlkalinityMotor.run(Adafruit_MotorHAT.FORWARD)
	AlkalinityMotor.run(Adafruit_MotorHAT.RELEASE)
except RuntimeError:
	print("Error creating motor objects. Is the Adafruit library installed and the HAT connected?")

# Create GPIO objects and configure
try:
	import RPi.GPIO as GPIO
except RuntimeError:
	print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")
GPIO.setmode(GPIO.BCM)
CalciumButtonPin = 22
AlkalinityButtonPin = 23
GPIO.setup(CalciumButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(AlkalinityButtonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Button event callback functions
def calciumevent(channel):
	print('Edge detected on channel %s'%channel)
	if GPIO.input(CalciumButtonPin) == GPIO.LOW:
		CalciumMotor.run(Adafruit_MotorHAT.FORWARD)
		CalciumMotor.setSpeed(255)
		print('Calcium pump on')
	else:
		CalciumMotor.run(Adafruit_MotorHAT.RELEASE)
		print('Calcium pump off')

def alkalinityevent(channel):
	print('Edge detected on channel %s'%channel)
	if GPIO.input(channel) == GPIO.LOW:
		AlkalinityMotor.run(Adafruit_MotorHAT.FORWARD)
		AlkalinityMotor.setSpeed(255)
		print('Alkalinity pump on')
	else:
		AlkalinityMotor.run(Adafruit_MotorHAT.RELEASE)
		print('Alkalinity pump off')

# Create button detection events
GPIO.add_event_detect(CalciumButtonPin, GPIO.BOTH, callback=calciumevent, bouncetime=200)
GPIO.add_event_detect(AlkalinityButtonPin, GPIO.BOTH, callback=alkalinityevent, bouncetime=200)

# Forever do nothing loop
while True:
	sleep(1)