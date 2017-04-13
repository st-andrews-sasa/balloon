from sense_hat import SenseHat

sense = SenseHat()
while 1:
    orientation = sense.get_orientation_degrees()
    print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
