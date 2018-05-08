#Libraries
import RPi.GPIO as GPIO
import time

class HCSR04 (object):

    def __init__(self, trigger, echo):
        # GPIO Mode (BOARD / BCM)
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
        beginningTime = time.time()
        while GPIO.input(self.GPIO_ECHO) == 0:
            StartTime = time.time()
            if (StartTime - beginningTime) > 1:
                # print "reseting"
                GPIO.cleanup()
                # print "cleanup done, sleeping for 1 sec"
                time.sleep(1)
                GPIO.setmode(GPIO.BCM)
                # print "mode set"
                GPIO.setup(self.GPIO_ECHO, GPIO.OUT)
                GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
                GPIO.output(self.GPIO_ECHO, False)
                # print "pins set, echo outputs false, waiting 0.5 s"
                time.sleep(1)

                GPIO.cleanup()
                # print "second cleanup done"
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(self.GPIO_ECHO, GPIO.IN)
                GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
                beginningTime = time.time()
                
                break
     
        # save time of arrival
        while GPIO.input(self.GPIO_ECHO) == 1:
            StopTime = time.time()
     
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 343000) / 2
        

        return distance

    def cleanupPins(self):
        GPIO.cleanup()
 
if __name__ == '__main__':
    try:
        print("starting")
        ultrasonic = HCSR04(16, 18)
        # ultrasonic = HCSR04(35, 37)

        while True:
            dist = ultrasonic.getDistance()
            print ("Measured getDistance = %.1f mm" % dist)
            time.sleep(0.1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()