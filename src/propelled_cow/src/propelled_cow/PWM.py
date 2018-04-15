import time
import RPi.GPIO as GPIO

class PWM:

	# constructor
    def __init__(self, pin):
    	self.pin = pin
    	self.pwm = GPIO.PWM(pin, 333) # 333 Hz


    def start(self, val): # in deg
        self.deg = float((self.max_val - self.min_val))/180
        self.set_angle = self.min_val + self.deg * angle
        print("setting angle: {}".format(angle))
        self.pwm.start(self.set_angle)

    def stop(self):
	   self.pwm.stop()

    def example(self): # in deg
        self.pwm.start(self.min_val)
        time.sleep(2)
        self.pwm.ChangeDutyCycle(self.max_val)
        time.sleep(2)
        self.pwm.stop()
        #GPIO.cleanup()

if(__name__ == '__main__'): # connect servo to the pin below
    pin = 11
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    servo = Servo(pin, min_val=4, max_val=6)
    servo.example()

