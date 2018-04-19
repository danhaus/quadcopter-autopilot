import time
import pigpio
# FIRST RUN sudo pigpiod in terminal
pin = 18
pi = pigpio.pi() # Connect to local Pi
pi.set_mode(pin, pigpio.OUTPUT)
pi.set_servo_pulsewidth(pin, 1000) # safe anti-clockwise
time.sleep(2)
pi.set_servo_pulsewidth(pin, 1500) # centre
time.sleep(2)
pi.set_servo_pulsewidth(pin, 2000) # safe clockwise
time.sleep(2)
pi.set_servo_pulsewidth(pin, 0) # swtich off
pi.stop()
