import time
import pigpio
# FIRST RUN sudo pigpiod in terminal
pin = 4
pi = pigpio.pi() # Connect to local Pi.
pi.set_mode(pin, pigpio.OUTPUT)
pi.set_servo_pulsewidth(17, 1000) # safe anti-clockwise
time.sleep(1)
pi.set_servo_pulsewidth(17, 1500) # centre
time.sleep(1)
pi.set_servo_pulsewidth(17, 2000) # safe clockwise
time.sleep(1)
pi.stop()