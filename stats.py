from sense_hat import SenseHat
import os
from time import sleep

sense = SenseHat()
while 1:
    orientation = sense.get_orientation_degrees()
    print("Pitch: {pitch}\nRoll: {roll}\nYaw: {yaw}".format(**orientation))
    print("---")
    temp = sense.get_temperature()
    print("Temperature: %s F" % temp*(9/5) + 32)
    print("---")
    humidity = sense.get_humidity()
    print("Humidity: %s %%rH" % humidity)
    sleep(0.1)
    os.system('clear')
