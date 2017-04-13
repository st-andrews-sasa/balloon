from sense_hat import SenseHat
import os
from time import sleep

sense = SenseHat()
while 1:
    orientation = sense.get_orientation_degrees()
    print("p: {pitch}\nr: {roll}\ny: {yaw}".format(**orientation))
    sleep(0.1)
    os.system('clear')
