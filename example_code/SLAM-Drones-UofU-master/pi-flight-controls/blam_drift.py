from ctrl import fc
from kinect_pose import Kinect_Odom
from ultrasonic import distance
import time
import RPi.GPIO as GPIO


class Takeoff:
    # Time to sleep between updates.
    sleep_time = 0.02
    # How quickly to accelerate motors from zero to takeoff speed. Units are throttle per second
    spin_up_speed = 50 * sleep_time
    # Final height to hover in centimeters
    hover_height = 27
    # Time for the copter to be in the air in seconds
    total_flight_time = 1.5
    # How fast to decrease throttle for landing. Throttle per second
    landing_speed = 100 * sleep_time
    # The throttle value that slowly and steadily increases the height of the copter
    takeoff_throttle = 1520
    # The approximate throttle to hover.
    hover_throttle = 1445 # TODO SWITCH EVERY BATTERY CHANGE
    #hover_throttle = 1490
    # Maximum distance from hover throttle possible while in hover mode
    max_throttle_adjustment = 75
    # Height to kill the motors at on the way back down
    landing_height = 10
    # If this amount of time passes in takeoff and we haven't reached the hover height, abort
    takeoff_timeout = 6
    # Change to pid at this percentage of the hover height
    pid_takeover = 0.8
    # Proportional parameter of PID. Units are Throttle per cm of error
    p = 25
    # Integral parameter of PID. Units are Throttle per cm of error per second
    i = .5
    # Derivative parameter of PID. Units are Throttle per change in cm per second
    d = 0

    def __init__(self, flight_controller):
        self.drift_correction = Kinect_Odom(f)
        self.dift_correction.listener()
        GPIO.cleanup()
        self.flight_controller = flight_controller
        self.throttle = 1350
        self.flight_controller.setThrottle(self.throttle)
        self.ultrasonic = distance()
        self.flight_time = 0
        self.timer = 0
        self.d = 0
        self.pid = 0

    def exit(self):
        self.flight_controller.disarm()
        time.sleep(4)

    def takeoff_and_hover(self):
        with open("flight_log.txt", "w") as myfile:
            # Increase throttle until we leave the ground at the takeoff speed
            myfile.write("Entering takeoff at time: 0\n")
            while self.d < Takeoff.hover_height * Takeoff.pid_takeover:
                if self.timer >= Takeoff.takeoff_timeout:
                    myfile.write("Disarmed\n")
                    self.exit()
                    return
                self.d = self.ultrasonic.distance()
                if self.throttle < Takeoff.takeoff_throttle:
                    self.throttle += Takeoff.spin_up_speed
                    self.flight_controller.setThrottle(int(self.throttle))
                self.timer += Takeoff.sleep_time
                myfile.write("Time: " + str(self.timer) + " Distance reading: " + str(self.d) + " Throttle: "
                             + str(self.throttle) + "\n")
                time.sleep(Takeoff.sleep_time)
            # Hover
            myfile.write("Entering hover at time: " + str(self.timer) + "\n")
            #self.flight_controller.setYaw(1450)
            self.pid = Pid(Takeoff.hover_height, Takeoff.sleep_time, Takeoff.p, Takeoff.i, Takeoff.d,
                           Takeoff.hover_height - Takeoff.hover_height * Takeoff.pid_takeover)
            while self.flight_time < Takeoff.total_flight_time and self.d > Takeoff.landing_height:
                self.d = self.ultrasonic.distance()
                adjustment = int(self.pid.get_correction(self.d))
                # Filter for bad values
                if self.d > 45 or self.d < 5:
                    adjustment = 0
                # Constrain throttle adjustments
                if adjustment > Takeoff.max_throttle_adjustment:
                    adjustment = Takeoff.max_throttle_adjustment
                elif adjustment < -Takeoff.max_throttle_adjustment:
                    adjustment = -Takeoff.max_throttle_adjustment
                self.throttle = Takeoff.hover_throttle + adjustment
                self.flight_controller.setThrottle(int(self.throttle))
                self.flight_time += Takeoff.sleep_time
                self.timer += Takeoff.sleep_time
                correction_str = "CORRECTIONS P: " + str(self.drift_correction.pitch_correction) + " R: " + str(self.drift_correction.roll_correction)
                myfile.write("Time: " + str(self.timer) + " Distance reading: " + str(self.d) + " Throttle adjustment: "
                             + str(adjustment) + " Throttle: " + str(self.throttle) + correction_str "\n")
                time.sleep(Takeoff.sleep_time)
            # Land
            #self.flight_controller.setYaw(1497)
            myfile.write("Entering landing at time: " + str(self.timer) + "\n")
            while self.d > Takeoff.landing_height and self.throttle > 1300:
                self.d = self.ultrasonic.distance()
                self.throttle -= Takeoff.landing_speed
                if self.throttle <= 1000:
                    self.throttle = 1000
                self.flight_controller.setThrottle(int(self.throttle))
                self.timer += Takeoff.sleep_time
                myfile.write("Time: " + str(self.timer) + " Distance reading: " + str(self.d) + " Throttle: "
                             + str(self.throttle) + "\n")
                time.sleep(Takeoff.sleep_time)
            # We have landed, kill throttle
            myfile.write("Disarmed\n")
            self.exit()


class Pid:
    def __init__(self, target, time_step, p, i, d, initial_error):
        self.ui = 0
        self.e_prev = initial_error
        self.target = target
        self.time_step = time_step
        self.p = p
        self.i = i
        self.d = d

    def get_correction(self, y):
        # Error between the desired and actual output
        e = self.target - y
        # Integration Input
        self.ui = (self.ui + self.time_step * e)
        # Derivation Input
        ud = (e - self.e_prev) / self.time_step
        # Adjust previous values
        self.e_prev = e
        # Calculate input for the system
        return self.p * e + self.i * self.ui + self.d * ud

if __name__ == "__main__":
    f = fc()
    # 1507,1499,1497
    f.setRoll(1514)
    f.setPitch(1495)
    f.setYaw(1497)

    test = Takeoff(f)
    test.takeoff_and_hover()
