#test

#Libraries import
import RPi.GPIO as GPIO
import time
from ultrasuoni import get_distance
from motori import *

debug=False

if __name__ == "__main__":
    while True:
        result1= get_distance(TRIG_PIN_1,ECHO_PIN_1)
        result2= get_distance(TRIG_PIN_2,ECHO_PIN_2)
        result3= get_distance(TRIG_PIN_3,ECHO_PIN_3)

        if debug:
            print(f"\nSensore 1: {result1}")
            print(f"\nSensore 2: {result2}")
            print(f"\nSensore 3: {result3}")




            
