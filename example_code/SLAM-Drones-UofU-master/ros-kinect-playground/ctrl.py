import thread
import time

from pyMultiwii import MultiWii


class FC:

    def __init__(self):
        self.data = [1500,1500,1500,1000,1000,1000,1000,1000]
        self.board = MultiWii("/dev/ttyUSB0")
        self.board.arm()
        thread.start_new_thread(self.run, ())
        self.MAX = 2000
        self.MIN = 1000

    def run(self):
        while True:
            self.board.sendCMD(16, MultiWii.SET_RAW_RC, self.data)
            time.sleep(0.05)

    def set_throttle(self, throttle):
        if throttle < self.MIN:
            throttle = self.MIN
        elif throttle > self.MAX:
            throttle = self.MAX

        self.data = self.data[:3] + [throttle] + self.data[4:]
        print self.data

    def set_roll(self, roll):
        if roll < self.MIN:
            roll = self.MIN
        elif roll > self.MAX:
            roll = self.MAX

        self.data = [roll] + self.data[1:]
        print self.data

    def set_pitch(self, pitch):
        if pitch < self.MIN:
            pitch = self.MIN
        elif pitch > self.MAX:
            pitch = self.MAX

        self.data = self.data[:1] + [pitch] + self.data[2:]
        print self.data

    def set_yaw(self, yaw):
        if yaw < self.MIN:
            yaw = self.MIN
        elif yaw > self.MAX:
            yaw = self.MAX

        self.data = self.data[:2] + [yaw] + self.data[3:]
        print self.data

    def get_throttle(self):
        return self.data[3]

    def get_roll(self):
        return self.data[0]

    def get_pitch(self):
        return self.data[1]

    def get_yaw(self):
        return self.data[2]

