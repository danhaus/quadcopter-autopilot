import time
import RPi.GPIO as GPIO
import signal

#Pin Numbers
GPIO_TRIGGER = 2
GPIO_ECHO = 3

if __name__ == "__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
    GPIO.output(GPIO_TRIGGER, False)
    time.sleep(0.5)
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()
    while GPIO.input(GPIO_ECHO) is 0:
        start = time.time()
    while GPIO.input(GPIO_ECHO) is 1:
        stop = time.time()
    #distance in cm
    distance = (stop-start) * 17000
    print "Distance: %.1f" % distance
    GPIO.cleanup()

class distance:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(GPIO_ECHO, GPIO.IN)
        GPIO.output(GPIO_TRIGGER, False)
        time.sleep(0.5)
        signal.signal(signal.SIGINT, self.cleanup)

    def cleanup(self, signal, frame):
        GPIO.cleanup()

    def distance(self):
        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
        start = time.time()
        while GPIO.input(GPIO_ECHO) is 0:
            start = time.time()
        while GPIO.input(GPIO_ECHO) is 1:
            stop = time.time()
        return (stop-start) * 17000
