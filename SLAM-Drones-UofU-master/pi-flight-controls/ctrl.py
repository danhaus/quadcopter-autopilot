import thread
import time

from pyMultiwii import MultiWii

class fc:

    def __init__(self):
        self.data = [1500,1500,1500,1000,1000,1000,1000,1000]
        self.board = MultiWii("/dev/ttyUSB0")
        self.board.arm()
	self.armed = 1
        thread.start_new_thread(self.run, (self,))

    def run(self, f):
        while(True):
            self.board.sendCMD(16,MultiWii.SET_RAW_RC,f.data)
	    if f.armed == 0:
		f.board.disarm()
            time.sleep(0.05)

    def setThrottle(self, throttle):
        self.data = self.data[:3] + [throttle] + self.data[4:]
        self.changed = True
        print self.data

    def setRoll(self, roll):
        self.data = [roll] + self.data[1:]
        print self.data

    def setPitch(self, pitch):
        self.data = self.data[:1] + [pitch] + self.data[2:]
        print self.data

    def setYaw(self, yaw):
        self.data = self.data[:2] + [yaw] + self.data[3:]
        print self.data
    
    def disarm(self):
	self.armed = 0
