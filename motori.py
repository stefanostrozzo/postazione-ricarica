#PROGRAMMA PER IL FUNZIONAMENTO DEI MOTORI

#Import librerie necessarie
import RPi.GPIO as GPIO
import time

def movimentazione(pwm,pin1,pin2,x,y):
    pass

def stop_motor(pwm):
    pwm.ChangeDutyCycle(0) #Put the DC to 0 to stop the motors

def encoder_count():
    pass
