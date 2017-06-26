import time
import Adafruit_PCA9685
from time import strftime
import os
import math
from decimal import *

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)

def run():
    servo_min = 200  # Min pulse length out of 4096
    servo_max = 500  # Max pulse length out of 4096
    servo_x = servo_min
    print('Moving servo on channel 0, press Ctrl-C to quit...')
    for num in range(0,1080000):
        servo_x = servo_x+0.000278
        print("servo_x: "+ str(servo_x))
        pwm.set_pwm(0, 0, int(servo_x))
        time.sleep(0.01)

def destroy():
    GPIO.cleanup()                     # Release resource

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        destroy()