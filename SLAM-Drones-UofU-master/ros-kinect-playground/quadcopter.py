#!/usr/bin/env python

from pyMultiwii import MultiWii
from sys import stdout
import time
from ctrl import FC


class Quadcopter:
    # TODO add variable to

    def __init__(self):
        print("Quadcopter")
        self.flight_controller = FC()
        self.throttle = self.flight_controller.get_throttle()
        self.yaw = self.flight_controller.get_yaw()
        self.pitch = self.flight_controller.get_pitch()
        self.roll = self.flight_controller.get_roll()

    def stop(self):
        print("Stopping")

    def move_forward(self, seconds):
        self.pitch = self.flight_controller.get_pitch()
        self.flight_controller.set_pitch(self.pitch+100)
        time.sleep(2)
        print("Moving forward " + str(seconds) + " seconds")

    def move_up(self, seconds):
        print("Moving up for 2 seconds")
        self.throttle = self.flight_controller.get_throttle()
        self.flight_controller.set_throttle(self.throttle+100)
        time.sleep(2)
        print("Stopped")

    def move_down(self, seconds):
        print("Moving down for 2 seconds")
        self.throttle = self.flight_controller.get_throttle()
        self.flight_controller.set_throttle(self.throttle-100)
        time.time.sleep(2)
        print("Stopped")

    def move_backward(self, seconds):
        print("Moving backward for " + str(seconds) + " seconds")
        self.pitch = self.flight_controller.get_pitch()
        self.flight_controller.set_pitch(self.pitch-100)
        time.time.sleep(2)
        print("Stopped")

    def move_left(self, seconds):
        print("Moving left " + str(seconds) + " seconds")
        self.roll = self.flight_controller.get_roll()
        self.flight_controller.set_roll(self.roll-100)
        time.sleep(2)
        print("Stopped")

    def move_right(self, seconds):
        print("Moving right " + str(seconds) + " seconds")
        self.roll = self.flight_controller.get_roll()
        self.flight_controller.set_roll(self.roll+100)
        time.sleep(2)
        print("Stopped")

    def rotate_right(self, degrees):
        print("Rotating right " + str(degrees) + " degrees")
        self.yaw = self.flight_controller.get_yaw()
        self.flight_controller.set_yaw(self.yaw+100)
        time.sleep(2)
        print("Stopped")

    def rotate_left(self, degrees):
        print("Rotating left " + str(degrees) + " degrees")
        self.yaw = self.flight_controller.get_yaw()
        self.flight_controller.set_yaw(self.yaw-100)
        time.sleep(2)
        print("Stopped")


    def face_north(self):
        print("Rotating to north")

    def begin_dissent(self):
        print("Begining dissent")
        # TODO throttle down slowly
        print("Done")
