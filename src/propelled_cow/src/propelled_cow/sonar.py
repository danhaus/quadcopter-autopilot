from datetime import datetime
import pigpio
import time

###########################
# USING BCM PIN NUMBERING #
###########################

class Sonar(object):

    def __init__(self, echo):

        self.start = 0
        self.stop = 0

        self.echo = echo
        self.pi = pigpio.pi()
        self.pi.set_pull_up_down(self.echo, pigpio.PUD_DOWN)
        self.cb1 = self.pi.callback(echo, pigpio.RISING_EDGE, self.cbf)
        self.cb2 = self.pi.callback(echo, pigpio.FALLING_EDGE, self.cbf2)

    def cbf(self, gpio, level, tick):
        # rising = tick
        # print(level)
        self.start = datetime.now()
        # return

    def cbf2(self, gpio, level, tick):
        self.stop = datetime.now()
        dif = (self.stop - self.start)
        dif_micro = dif.microseconds
        # dist = dif_micro // 147
        print dif_micro
        # print(level)

 
if __name__ == '__main__':
    print "started"
    sonar = Sonar(23)
    while True:
        pass