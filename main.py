#Libraries import
import RPi.GPIO as GPIO
import time
from ultrasuoni import get_distance
import concurrent.futures

#GPIO configuration
GPIO.setmode(GPIO.BCM)

#Ultrasound sensors
#Sensor 1
TRIG_PIN_1= 17
ECHO_PIN_1= 14

#Sensor 2
TRIG_PIN_2= 27
ECHO_PIN_2= 15

#Sensor 3
TRIG_PIN_3= 22
ECHO_PIN_3= 18


#Setting all I/O
#Ultrasound sensors
#Sensor 1
GPIO.setup(TRIG_PIN_1, GPIO.OUT)
GPIO.setup(ECHO_PIN_1, GPIO.IN)

#Sensor 2
GPIO.setup(TRIG_PIN_2, GPIO.OUT)
GPIO.setup(ECHO_PIN_2, GPIO.IN)

#Sensor 3
GPIO.setup(TRIG_PIN_3, GPIO.OUT)
GPIO.setup(ECHO_PIN_3, GPIO.IN)


if __name__ == "__main__":
    while True:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            thread_ultrasound1=executor.submit(get_distance, TRIG_PIN_1, ECHO_PIN_1)
            result1 = thread_ultrasound1.result()
        
            print(f"\nSensore 1: {result1}")

        with concurrent.futures.ThreadPoolExecutor() as executor:
            thread_ultrasound2=executor.submit(get_distance, TRIG_PIN_2, ECHO_PIN_2)
            result2 = thread_ultrasound2.result()
        
            print(f"\nSensore 2: {result2}")
        
        with concurrent.futures.ThreadPoolExecutor() as executor:
            thread_ultrasound3=executor.submit(get_distance, TRIG_PIN_3, ECHO_PIN_3)
            result3 = thread_ultrasound3.result()
        
            print(f"\nSensore 3: {result3}")


            