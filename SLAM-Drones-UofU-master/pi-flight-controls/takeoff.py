from ctrl import fc
from ultrasonic import distance
import time
import RPi.GPIO as GPIO


class Takeoff:
    # Time to sleep between updates.
    sleep_time = 0.05
    # How quickly to accelerate motors from zero to takeoff speed. Units are throttle per second
    spin_up_speed = 50 * sleep_time
    # How fast to go from the ground to hover height. Units are centimeters per second
    take_off_speed = 1 * sleep_time
    # This should be just higher than the distance measurement when copter is on ground.
    # When the distance measurement is higher than this, it is assumed that throttle reach
    # a point where we have just started leaving the ground. Units are centimeters
    resting_height = 7.5
    # Final height to hover in centimeters
    hover_height = 10
    # Throttle increase per distance from target height in centimeters.
    # Ex: This value is 10, if we are 4cm below target height, increase throttle by 40
    proportion_constant = 1 
    # Time for the copter to be in the air in seconds
    total_flight_time = 2 
    # How fast to decrease throttle for landing. Throttle per second
    landing_speed = 30 * sleep_time

    def __init__(self, flight_controller):
	GPIO.cleanup()
        self.flight_controller = flight_controller
        self.throttle = 1350
        self.flight_controller.setThrottle(self.throttle)
        self.ultrasonic = distance()
        self.current_target_height = Takeoff.resting_height
        self.flight_time = 0
        self.timer = 0
        self.takeoff_filter_threshold = 3
        self.land_filter_threshold = 3

    def takeoff_and_hover(self):
        with open("flight_log.txt", "a") as myfile:
            # Increase throttle until we leave the ground at the takeoff speed
            myfile.write("Entering takeoff at time: 0\n")
            filter_count = 0
            # Wait until we have recorded a certain number (the threshold) of readings before continuing
            while filter_count < self.takeoff_filter_threshold:
                d = self.ultrasonic.distance() 
		if d >= Takeoff.resting_height:
                    filter_count += 1
                else:
                    filter_count = 0
                self.throttle += Takeoff.spin_up_speed
                myfile.write("Time: " + str(self.timer) + " Distance reading: " + str(d) + " Throttle: "
                             + str(self.throttle) + "\n")
                self.flight_controller.setThrottle(int(self.throttle))
                time.sleep(Takeoff.sleep_time)
                self.timer += Takeoff.sleep_time
            # Hover
            myfile.write("Entering hover at time: " + str(self.timer) + "\n")
            while self.flight_time < Takeoff.total_flight_time:
                current_height = self.ultrasonic.distance()
                # Current target height increases linearly at specified speed until it hits the target hover height
                if self.current_target_height < Takeoff.hover_height:
                    self.current_target_height += Takeoff.take_off_speed
                # Proportional control of throttle depending on distance of quad-copter from its target height
                proportional_adjustment = int((self.current_target_height - current_height) * Takeoff.proportion_constant)
                self.throttle += proportional_adjustment
                myfile.write("Time: " + str(self.timer) + " Distance reading: " + str(current_height)
                             + " Target Distance: " + str(self.current_target_height) + " Throttle adjustment: "
                             + str(proportional_adjustment) + " Throttle: " + str(self.throttle) + "\n")
                if self.throttle <= 1000:
                    self.throttle = 1000 
		self.flight_controller.setThrottle(int(self.throttle))
                self.flight_time += Takeoff.sleep_time
                time.sleep(Takeoff.sleep_time)
                self.timer += Takeoff.sleep_time
            # Land
            myfile.write("Entering landing at time: " + str(self.timer) + "\n")
            filter_count = 0
            # Wait until we have recorded a certain number (the threshold) of readings before continuing
            while filter_count < self.land_filter_threshold:
		d = self.ultrasonic.distance()	
		if d <= Takeoff.resting_height:
                    filter_count += 1
                else:
                    filter_count = 0
                myfile.write("Time: " + str(self.timer) + " Distance reading: " + str(d) + " Throttle: "
                             + str(self.throttle) + "\n")
                if self.throttle <= 1200:
			break 
		self.throttle -= Takeoff.landing_speed
		if self.throttle <= 1000:
			self.throttle = 1000
                self.flight_controller.setThrottle(int(self.throttle))
                time.sleep(Takeoff.sleep_time)
                self.timer += Takeoff.sleep_time
            # We have landed, kill throttle
	    self.flight_controller.disarm()

if __name__ == "__main__":
    f = fc()
    # TODO: Set trim values here
    f.setRoll(1494)
    f.setPitch(1510)
    f.setYaw(1503)
    test = Takeoff(f)
    test.takeoff_and_hover()
