import time
import RPi.GPIO as GPIO

class Servo:
	# constructor
    def __init__(self, pin, max_right=5, max_left=10):
    	self.pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)
        self.max_right = max_right
        self.max_left = max_left
    	self.pwm = GPIO.PWM(pin, 50)


    def setAngle(self, angle): # in deg
        self.deg = float((self.max_left - self.max_right))/180
        self.set_angle = self.max_right + self.deg * angle
        print("setting angle: {}".format(angle))
        self.pwm.start(self.set_angle)

    def stop(self):
        self.pwm.stop()

    def example(self): # in deg
        self.pwm.start(self.max_right)
        time.sleep(5)
        self.pwm.ChangeDutyCycle(self.max_left)
        time.sleep(5)
        self.pwm.stop()
        #GPIO.cleanup()

if(__name__ == '__main__'): # connect servo to the pin below
    pin = 12
    servo = Servo(pin, max_right=5, max_left=10)
    servo.example()
    GPIO.cleanup()

