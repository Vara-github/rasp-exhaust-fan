#ThingSpeak Charts and Fan Control System

This project is a web and hardware integration that displays ThingSpeak charts on a webpage and controls a fan using a Raspberry Pi based on temperature readings from a DHT22 sensor. The temperature data and fan speed are sent to ThingSpeak for real-time monitoring.

#Prerequisites
Raspberry Pi
DHT22 sensor
Fan with PWM control
Python 3.x
Internet connection for Raspberry Pi
ThingSpeak account and API key

#Install the required Python libraries: pip install RPi.GPIO Adafruit_DHT requests

#Connect the DHT22 sensor to the Raspberry Pi:
VCC to 3.3V
GND to Ground
Data to GPIO4 (pin 7 on Raspberry Pi)

#Connect the fan to the Raspberry Pi:
PWM pin to GPIO18 (pin 12 on Raspberry Pi)
Power and Ground as needed
