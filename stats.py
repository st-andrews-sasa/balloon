from sense_hat import SenseHat
import os
from time import sleep

sense = SenseHat()
while 1:
    orientation = sense.get_orientation_degrees()
    print("Pitch: {pitch}\nRoll: {roll}\nYaw: {yaw}".format(**orientation))
    print("---")
    temp = sense.get_temperature()
    print("Temperature: %s C" % temp)
    print("---")
    humidity = sense.get_humidity()
    print("Humidity: %s %%rH" % humidity)
    pressure = sense.get_pressure()
    print('Pressure:', pressure)
    compass = sense.get_compass()
    print('Compass:', compass)
    print("---")
    accel_only = sense.get_accelerometer_raw()
    print("x: {x}\ny: {y}\nz: {z}".format(**accel_only))
    sleep(0.2)
    os.system('clear')
