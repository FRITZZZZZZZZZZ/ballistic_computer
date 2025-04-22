from mpu6050egg_sample import mpu6050
import time
sensor = mpu6050(0x68)
while True:
    accelerometer_data = sensor.get_accel_data()
    print(accelerometer_data)
    time.time(0.1)
    