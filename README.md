#ThingSpeak Charts and Fan Control System <br />

This project is a web and hardware integration that displays ThingSpeak charts on a webpage and controls a fan using a Raspberry Pi based on temperature readings from a DHT22 sensor. The temperature data and fan speed are sent to ThingSpeak for real-time monitoring. <br /><br />

#Components used <br />

Raspberry Pi  <br />
DHT22 sensor  <br />
Fan with PWM control  <br />
Python 3.x  <br />
Internet connection for Raspberry Pi  <br />
ThingSpeak account and API key <br />

#Install the required Python libraries: <br />

pip install RPi.GPIO Adafruit_DHT requests  <br /><br />

#Connect the DHT22 sensor to the Raspberry Pi:  <br />  
VCC to 3.3V  <br />
GND to Ground  <br />
Data to GPIO4 (pin 7 on Raspberry Pi)   <br />

#Connect the fan to the Raspberry Pi:   <br />
PWM pin to GPIO18 (pin 12 on Raspberry Pi)  <br />
Power and Ground as needed  
