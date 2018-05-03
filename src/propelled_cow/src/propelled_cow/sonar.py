import time
import pigpio

###########################
# USING BCM PIN NUMBERING #
###########################

class Sonar(object):

    def __init__(self, echo):

        self.start = 0
        self.stop = 0

        self.echo = echo
        self.pi = pigpio.pi()
        self.pi.set_mode(self.echo, pigpio.INPUT)
        self.pi.set_pull_up_down(self.echo, pigpio.PUD_DOWN)
        self.cb1 = self.pi.callback(echo, pigpio.RISING_EDGE, self.cbf)
        self.cb2 = self.pi.callback(echo, pigpio.FALLING_EDGE, self.cbf2)

    def cbf(self, gpio, level, tick):
        # rising = tick
        # print(rising)
        self.start = time.time()
        # return

    def cbf2(self, gpio, level, tick):
        self.stop = time.time()
        dif = self.stop - self.start
        print dif

 
if __name__ == '__main__':
    print "started"
    sonar = Sonar(18)
    while True:
        pass