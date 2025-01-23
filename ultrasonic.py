import RPi.GPIO as GPIO
import time

TRIGGER_PIN = 10
ECHO_PIN = 11

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIGGER_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def measure_distance():
    GPIO.output(TRIGGER_PIN, GPIO.LOW)
    time.sleep(0.000002)

    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)

    while GPIO.input(ECHO_PIN) == 0:
        t_off = time.time()

    while GPIO.input(ECHO_PIN) == 1:
        t_on = time.time()

    t = t_on - t_off

    dist_cm = (t * 34300) / 2      #Abstand[cm]=(Zeit[s] * Schallgeschwindigkeit[cm/s])/2
    return dist_cm

while True:
   dist = measure_distance()
   print(f"Abstand: {dist:.2f} cm")
   time.sleep(0.5)

