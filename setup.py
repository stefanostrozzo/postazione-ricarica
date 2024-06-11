#Setup for the entire program
import RPi.GPIO as GPIO
import time
#from motori import encoder_count

global pwm1,pwm2,pwm3, TRIG_PIN_1, ECHO_PIN_1

def encoder_count():
  pass

def setup():
  GPIO.setwarnings(False)
  #GPIO configuration
  GPIO.setmode(GPIO.BCM)
  
  #Motors
  #Motor 1
  PWM1=12
  M1P1=16 #It means Motor1 Pin1
  M1P2=20
  
  #Motor2
  PWM2=13
  M2P1=5
  M2P2=6

  #Motor3 It's the vertical movement
  PWM3=11
  M3P1=10
  M3P2=9
  
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
  #Motors
  #PWM
  GPIO.setup(PWM1,GPIO.OUT)
  pwm1 = GPIO.PWM(PWM1,100)
  pwm1.start(0)
  
  GPIO.setup(PWM2,GPIO.OUT)
  pwm2 = GPIO.PWM(PWM2,100)
  pwm2.start(0)

  GPIO.setup(PWM3,GPIO.OUT)
  pwm3 = GPIO.PWM(PWM3,100)
  pwm3.start(0)
  #Motors Inputs
  GPIO.setup(M1P1,GPIO.OUT)
  GPIO.setup(M1P2,GPIO.OUT)

  GPIO.setup(M2P1,GPIO.OUT)
  GPIO.setup(M2P2,GPIO.OUT)

  GPIO.setup(M3P1,GPIO.OUT)
  GPIO.setup(M3P2,GPIO.OUT)
  
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
  #Encoder 1
  GPIO.add_event_detect(ENC1_F1, GPIO.RISING, callback=encoder_count)
  GPIO.add_event_detect(ENC1_F2, GPIO.RISING, callback=encoder_count)
  
  #Encoder 2
  GPIO.add_event_detect(ENC2_F1, GPIO.RISING, callback=encoder_count)
  GPIO.add_event_detect(ENC2_F2, GPIO.RISING, callback=encoder_count)

print("!Setup completed!")
