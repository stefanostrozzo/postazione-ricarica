#Setup for the entire program
import RPi.GPIO as GPIO
import time
from motori import encoder_count

def setup():
  #GPIO configuration
  GPIO.setmode(GPIO.BCM)
  
  #Ultrasound sensors
  #Sensor 1
  TRIG_PIN_1 = 17
  ECHO_PIN_1 = 14
  
  #Sensor 2
  TRIG_PIN_2 = 27
  ECHO_PIN_2 = 15
  
  #Sensor 3
  TRIG_PIN_3 = 22
  ECHO_PIN_3 = 18
  
  #Encoders
  #Encoder 1
  ENC1_F1 = 25
  ENC1_F2 = 8
  
  #Encoder 2
  ENC2_F1 = 1
  ENC2_F2 = 7
  
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
  
  #Encoders
  #Encoder 1
  GPIO.setup(ENC1_F1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(ENC1_F2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  
  #Encoder 2
  GPIO.setup(ENC2_F1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(ENC2_F2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  
  #Interrupt
  #Count function is the function inside motori.py that counts how many times the encoder raises it's value
  #Encoder 1
  GPIO.add_event_detect(ENC1_F1, GPIO.RISING, callback=encoder_count)
  GPIO.add_event_detect(ENC1_F2, GPIO.RISING, callback=encoder_count)
  
  #Encoder 2
  GPIO.add_event_detect(ENC2_F1, GPIO.RISING, callback=encoder_count)
  GPIO.add_event_detect(ENC2_F2, GPIO.RISING, callback=encoder_count)
