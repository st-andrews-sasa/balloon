from sense_hat import SenseHat
import os

sense = SenseHat()
while 1:
    orientation = sense.get_orientation_degrees()
    print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
    os.system('clear')
