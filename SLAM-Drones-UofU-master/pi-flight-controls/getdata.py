import thread
import time
from ultrasonic import distance

from pyMultiwii import MultiWii


class fc:

    def __init__(self):
        self.data = [1500,1500,1500,1000,1000,1000,1000,1000]
        self.board = MultiWii("/dev/ttyUSB0")
        self.start = time.time()
        self.distance = distance()
        #self.board.arm()
        thread.start_new_thread(self.run, ())

    def run(self):
        while(True):
            self.board.getData(MultiWii.RC)
            elapsed = time.time() - self.start
            s = str(self.board.rcChannels['roll']) + "," +  str(self.board.rcChannels['pitch']) + "," + str(self.board.rcChannels['yaw']) + "," +  str(self.board.rcChannels['throttle']) + "," + str(self.distance.distance())
            with open("data.txt", "a") as myfile:
                myfile.write(s + "\n")
            time.sleep(0.05)

    def setThrottle(self, throttle):
        self.data = self.data[:3] + [throttle] + self.data[4:]
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


if __name__ == "__main__":
    f = fc()
