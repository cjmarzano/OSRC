OSRC
====

Open Source Reef Controller powered by Raspberry Pi

Features include:
- Temperature measurement
- Dosing pump control and scheduling
- Thingspeak integration (Free cloud based IoT data logging)

Required Hardware:
- Raspberry Pi Model B+, Pi 2, or Pi 3

Optional Hardware:
- DS18B20 1-Wire Temperature Sensor
- RasClock Real Time Clock
- Adafruit Motor HAT
- Peristaltic Dosing Pump
- Buttons (for manually running pump)

Each script can be executed via crontab.
- startup.py pushes a status update to Thingspeak notifying the Pi is online.
- templogger.py reads a DS18B20 temperature sensor and pushes the data to Thingspeak for logging. Run at your desired measurement interval.
- dosingpumpbuttons.py should run at boot for manually running dosing pumps on a button press. A future update will dose automatically.
