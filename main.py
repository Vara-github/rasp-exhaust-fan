import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import requests
GPIO.setmode(GPIO.BCM)
FAN_PIN = 18

GPIO.setup(FAN_PIN, GPIO.OUT)
fan_pwm = GPIO.PWM(FAN_PIN, 1000)  
fan_pwm.start(0)  

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4 


THINGSPEAK_API_KEY = 'LTKEPDIBT919BJBM'
THINGSPEAK_URL = 'https://api.thingspeak.com/update'

def send_to_thingspeak(temp, fan_speed):
    payload = {'api_key': THINGSPEAK_API_KEY, 'field1': temp, 'field2': fan_speed}
    response = requests.post(THINGSPEAK_URL, data=payload)
    if response.status_code == 200:
        print("Data sent to ThingSpeak successfully")
    else:
        print("Failed to send data to ThingSpeak")

try:
    while True:
       
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

        if temperature is not None:
           
            if temperature < 25:
                fan_pwm.ChangeDutyCycle(0)  
                fan_speed = 0
            elif temperature >= 25 and temperature < 30:
                fan_pwm.ChangeDutyCycle(50) 
                fan_speed = 50
            else:
                fan_pwm.ChangeDutyCycle(100) 
                fan_speed = 100
            
           
            send_to_thingspeak(temperature, fan_speed)

        time.sleep(5)  
except KeyboardInterrupt:
    fan_pwm.stop()
    GPIO.cleanup()
