import time
import board
import busio
from adafruit_seesaw.seesaw import Seesaw

i2c_bus = busio.I2C(board.SCL, board.SDA)
ss = Seesaw(i2c_bus, addr=0x36)

while True:
    # read moisture level through capacitive touch pad
    touch = ss.moisture_read()
    # read temperature from the temperature sensor
    temp = ss.get_temp()
    print("temp: " + str(temp) + " moisture: " + str(touch))
    if touch < 400:
        print("Aaaaaah, gib mir Wasser!!!")
    if touch > 400 and touch < 1000: 
        print("Angenehm!!!")
    elif touch > 1000:
        print("Hiilfe, ich ertrinke!!!")
    time.sleep(1)