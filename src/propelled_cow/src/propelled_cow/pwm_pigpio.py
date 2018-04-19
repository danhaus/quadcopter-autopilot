import time
import pigpio

# FIRST RUN sudo pigpiod in terminal

class Servo:
	def __init__(self, pin, min_val=800, max_val=1800): # vals in us
		self.pin = pin
		self.pi = pigpio.pi()
		self.pi.set_mode(self.pin, pigpio.OUTPUT)
		self.min= min_val
		self.max = max_val

	def setAngle(self, angle):
		deg = float(self.max-self.min)/180
		duty_cycle = self.min + deg*angle
		self.pi.set_servo_pulsewidth(self.pin, duty_cycle)

	def stop(self):
		self.pi.set_servo_pulsewidth(self.pin, 0)
		self.pi.stop()

	def example(self):
		self.pi.set_servo_pulsewidth(self.pin, self.min) # safe anti-clockwise
		time.sleep(2)
		self.pi.set_servo_pulsewidth(self.pin, (self.max+self.min)/2) # centre
		time.sleep(2)
		self.pi.set_servo_pulsewidth(self.pin, self.max) # safe clockwise
		time.sleep(2)
		self.stop()

if __name__ == '__main__':
	pin = 4
	servo = Servo(pin)
	servo.example()