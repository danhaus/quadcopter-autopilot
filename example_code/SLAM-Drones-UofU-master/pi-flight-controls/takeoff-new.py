from ctrl import fc
from ultrasonic import distance
import time
import RPi.GPIO as GPIO


class Takeoff:
    # Time to sleep between updates.
    sleep_time = 0.05
    # How quickly to accelerate motors from zero to takeoff speed. Units are throttle per second
    spin_up_speed = 50 * sleep_time
    # Final height to hover in centimeters
    hover_height = 20
    # Time for the copter to be in the air in seconds
    total_flight_time = 4
    # How fast to decrease throttle for landing. Throttle per second
    landing_speed = 25 * sleep_time
    # The throttle value that slowly and steadily increases the height of the copter
    takeoff_throttle = 1500
    # The throttle value that causes the copter to hover at a constant height
    hover_throttle = 1450
    # Height to kill the motors at on the way back down
    landing_height = 12
    # Proportional parameter of PID. Units are Throttle per cm of error
    p = 1
    # Integral parameter of PID. Units are Throttle per cm of error per second
    i = 0
    # Derivative parameter of PID. Units are Throttle per change in cm per second
    d = 0

    def __init__(self, flight_controller):
        GPIO.cleanup()
        self.flight_controller = flight_controller
        self.throttle = 1350
        self.flight_controller.setThrottle(self.throttle)
        self.ultrasonic = distance()
        self.flight_time = 0
        self.timer = 0
        self.d = 0
        self.pid = Pid(Takeoff.hover_height, Takeoff.sleep_time, Takeoff.p, Takeoff.i, Takeoff.d)

    def takeoff_and_hover(self):
        with open("flight_log.txt", "a") as myfile:
            # Increase throttle until we leave the ground at the takeoff speed
            myfile.write("Entering takeoff at time: 0\n")
            while self.d < Takeoff.hover_height:
                self.d = self.ultrasonic.distance()
                if self.throttle < Takeoff.takeoff_throttle:
                    self.throttle += Takeoff.spin_up_speed
                    self.flight_controller.setThrottle(int(self.throttle))
                self.timer += Takeoff.sleep_time
                myfile.write("Time: " + str(self.timer) + " Distance reading: " + str(self.d) + " Throttle: "
                             + str(self.throttle) + "\n")
                time.sleep(Takeoff.sleep_time)
            # Hover
            self.flight_controller.setThrottle(Takeoff.hover_throttle)
            myfile.write("Entering hover at time: " + str(self.timer) + "\n")
            while self.flight_time < Takeoff.total_flight_time:
                self.d = self.ultrasonic.distance()
                # PID control of throttle depending on distance of quad-copter from its hover height
                adjustment = int(self.pid.get_correction(self.d))
                self.throttle += adjustment
                self.flight_controller.setThrottle(int(self.throttle))
                self.flight_time += Takeoff.sleep_time
                self.timer += Takeoff.sleep_time
                myfile.write("Time: " + str(self.timer) + " Distance reading: " + str(self.d) + " Throttle adjustment: "
                             + str(adjustment) + " Throttle: " + str(self.throttle) + "\n")
                time.sleep(Takeoff.sleep_time)
            # Land
            myfile.write("Entering landing at time: " + str(self.timer) + "\n")
            while self.d > Takeoff.landing_height and self.throttle > 1300:
                self.d = self.ultrasonic.distance()
                self.throttle -= Takeoff.landing_speed
                self.flight_controller.setThrottle(int(self.throttle))
                self.timer += Takeoff.sleep_time
                myfile.write("Time: " + str(self.timer) + " Distance reading: " + str(self.d) + " Throttle: "
                             + str(self.throttle) + "\n")
                time.sleep(Takeoff.sleep_time)
            # We have landed, kill throttle
            self.flight_controller.disarm()


class Pid:
    def __init__(self, target, time_step, p, i, d):
        self.ui = 0
        self.e_prev = 0
        self.target = target
        self.time_stamp = time_step
        self.p = p
        self.i = i
        self.d = d

    def get_correction(self, y):
        # Error between the desired and actual output
        e = self.target - y
        # Integration Input
        self.ui = (self.ui + self.time_stamp * e)
        # Derivation Input
        ud = (e - self.e_prev) / self.time_stamp
        # Adjust previous values
        self.e_prev = e
        # Calculate input for the system
        return self.p * e + self.i * self.ui + self.d * ud

if __name__ == "__main__":
    f = fc()
    # TODO: Set trim values here
    f.setRoll(1494)
    f.setPitch(1510)
    f.setYaw(1503)
    test = Takeoff(f)
    test.takeoff_and_hover()
