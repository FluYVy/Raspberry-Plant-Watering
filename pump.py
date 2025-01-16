import RPi.GPIO as GPIO
import time

IN1 = 2
IN2 = 3

GPIO.setmode(GPIO.BCM)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)

print("Motor läuft...")
GPIO.output(IN1, GPIO.HIGH)
GPIO.output(IN2, GPIO.LOW)

time.sleep(5)

print("Motor stoppt...")
GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)

