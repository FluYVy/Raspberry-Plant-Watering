import RPi.GPIO as GPIO
import time

IN1 = 14
IN2 = 15

GPIO.setmode(GPIO.BCM)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

#PWM für Pumpgeschwindikeit
pwm = GPIO.PWM(IN1, 100)    #100 Hz Frequenz
pwm.start(0) 

def pump_set_speed(speed):   #Geschwindikeit (0-100)
    GPIO.output(IN2, GPIO.LOW)
    pwm.ChangeDutyCycle(speed)

def pump_stop():
    pwm.ChangeDutyCycle(0)

pump_set_speed(30)
time.sleep(3)
pump_set_speed(60)
time.sleep(3)
pump_set_speed(90)
time.sleep(3)
pump_set_speed(100)
time.sleep(3)

