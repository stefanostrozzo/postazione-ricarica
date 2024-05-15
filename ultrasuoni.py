#Ultrasuoni

#Import librerie necessarie
import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

#Funzione che ritorna la distanza in cm
def get_distance(TRIG_PIN,ECHO_PIN):
    # Trigger pulse
    GPIO.output(TRIG_PIN, False)
    #print("basso")
    time.sleep(1)
    GPIO.output(TRIG_PIN, True)
    #print("alto")
    time.sleep(0.001)
    GPIO.output(TRIG_PIN, False)
    #print("basso")

    # Measure pulse duration
    pulse_end = time.time()
    pulse_start = time.time()

    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()
    
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    # Calculate distance (in cm)
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    
    return distance