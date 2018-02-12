#Libraries
import RPi.GPIO as GPIO
import time

class HCSR04 (object):

    def __init__(self, trigger=18, echo=24):
        #GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)
         
        #set GPIO Pins
        self.GPIO_TRIGGER = trigger
        self.GPIO_ECHO = echo
         
        #set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)
 
    def getDistance(self):
        # set Trigger to HIGH
        GPIO.output(self.GPIO_TRIGGER, True)
     
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(self.GPIO_TRIGGER, False)
     
        StartTime = time.time()
        StopTime = time.time()
     
        # save StartTime
        while GPIO.input(self.GPIO_ECHO) == 0:
            StartTime = time.time()
     
        # save time of arrival
        while GPIO.input(self.GPIO_ECHO) == 1:
            StopTime = time.time()
     
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
     
        return distance
 
if __name__ == '__main__':
    try:
        ultrasonic = HCSR04(18, 24)
        while True:
            dist = ultrasonic.getDistance()
            print ("Measured getDistance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()