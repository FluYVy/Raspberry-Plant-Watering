import time
import board
import busio
from adafruit_seesaw.seesaw import Seesaw

i2c_bus = busio.I2C(board.SCL, board.SDA)
ss = Seesaw(i2c_bus, addr=0x36)

def read_moisture():
    # returns calue between 200 (very dry) and 2000 (very wet)
    touch = ss.moisture_read()
    return touch

def read_temp():
    temp = ss.get_temp()
    return temp

while True:
    moisture = read_moisture()
    temp = read_temp()

    print("temp: " + str(temp) + " moisture: " + str(moisture))
    if moisture < 400:
        print("Aaaaaah, gib mir Wasser!!!")
    if moisture > 400 and moisture < 1000: 
        print("Angenehm!!!")
    elif moisture > 1000:
        print("Hiilfe, ich ertrinke!!!")
    time.sleep(1)