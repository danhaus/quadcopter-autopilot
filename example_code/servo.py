#!/usr/bin/env python
 
import time
 
import pigpio
 
servos = 4 #GPIO number
 
pigpio.start()
#pulsewidth can only set between 500-2500
try:
    while True:
 
        pigpio.set_servo_pulsewidth(servos, 500) #0 degree
        print("Servo {} {} micro pulses".format(servos, 1000))
        time.sleep(1)
        pigpio.set_servo_pulsewidth(servos, 1500) #90 degree
        print("Servo {} {} micro pulses".format(servos, 1500))
        time.sleep(1)
        pigpio.set_servo_pulsewidth(servos, 2500) #180 degree
        print("Servo {} {} micro pulses".format(servos, 2000))
        time.sleep(1)
        pigpio.set_servo_pulsewidth(servos, 1500)
        print("Servo {} {} micro pulses".format(servos, 1500))
        time.sleep(1)
 
   # switch all servos off
except KeyboardInterrupt:
    pigpio.set_servo_pulsewidth(servos, 0);
 
pigpio.stop()