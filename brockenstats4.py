##### Libraries #####
from datetime import datetime
from sense_hat import SenseHat
from time import sleep
from threading import Thread


##### Logging Settings #####


FILENAME = ""
WRITE_FREQUENCY = 1
TEMP_H=True
TEMP_P=False
HUMIDITY=True
PRESSURE=True
ORIENTATION=True
ACCELERATION=True
MAG=True
GYRO=True
DELAY=0.000000000000000000000000000000000000000000000000000000000000000000001 # how many seconds it should wait between data

def log_data():
  output_string = ",".join(str(value) for value in sense_data)
  batch_data.append(output_string)

def file_setup(filename):
  header  =["temp_h","temp_p","humidity","pressure",
  "pitch","roll","yaw",
  "mag_x","mag_y","mag_z",
  "accel_x","accel_y","accel_z",
  "gyro_x","gyro_y","gyro_z",
  "timestamp"]

  with open(filename,"w") as f:
      f.write(",".join(str(value) for value in header)+ "\n")


#####  Function  #####
      
def timed_log():
    while True:
      log_data()
      sleep(DELAY)


def get_sense_data():
    sense_data=[]

    sense_data.append(sense.get_temperature_from_humidity())
    sense_data.append(sense.get_temperature_from_pressure())
    sense_data.append(sense.get_humidity())
    sense_data.append(sense.get_pressure())

    o = sense.get_orientation()
    yaw = o["yaw"]
    pitch = o["pitch"]
    roll = o["roll"]
    sense_data.extend([pitch,roll,yaw])

    mag = sense.get_compass_raw()
    mag_x = mag["x"]
    mag_y = mag["y"]
    mag_z = mag["z"]
    sense_data.extend([mag_x,mag_y,mag_z])

    acc = sense.get_accelerometer_raw()
    x = acc["x"]
    y = acc["y"]
    z = acc["z"]
    sense_data.extend([x,y,z])

    gyro = sense.get_gyroscope_raw()
    gyro_x = gyro["x"]
    gyro_y = gyro["y"]
    gyro_z = gyro["z"]
    sense_data.extend([gyro_x,gyro_y,gyro_z])

    sense_data.append(datetime.now())

    return sense_data





#####  Main Program #####

sense = SenseHat()


batch_data= []

if FILENAME == "":
  filename = "SenseLog-"+str(datetime.now())+".csv"
else:
  filename = FILENAME+"-"+str(datetime.now())+".csv"


file_setup(filename)

if DELAY > 0:
  sense_data = get_sense_data()
  Thread(target= timed_log).start()
  
while True:
  sense_data = get_sense_data()
  sleep(DELAY)

  if len(batch_data) >= WRITE_FREQUENCY:
      print("Writing to file..")
      with open(filename,"a") as f:
          for line in batch_data:
              f.write(line + "\n")
          batch_data = []
