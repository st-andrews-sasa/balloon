from sense_hat import SenseHat
import os
from time import sleep

sense = SenseHat()
while 1:
    orientation = sense.get_orientation_degrees()
    print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
    sleep(1)
    os.system('clear')
