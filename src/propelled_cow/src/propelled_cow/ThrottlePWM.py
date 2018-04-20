import time
from propelled_cow.pwm_pigpio import PWM

class ThrottlePWM:

	# constructor
    def __init__(self, pin, freq=333, length=3000): # 333 Hz, 3000 us
    	self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
    	self.pwm = GPIO.PWM(pin, freq)
        self.length = length # length of the whole cycle in us
        self.start(0)

    def start(self, val=0):
        self.pwm.start(val)

    def stop(self):
	   self.pwm.stop()

    def changeDutyCycle(self, dutyTime):
        dutyCycle = dutyTime/self.length
        self.pwm.ChangeDutyCycle(dutyCycle)

if(__name__ == '__main__'): # connect servo to the pin below
    pass

