import time
import pigio

###########################
# USING BCM PIN NUMBERING #
###########################

class Sonar(object):

    def __init__(self, echo):

        self.echo = echo
        self.pi = pigpio.pi()
        self.pi.set_mode(self.echo, pigpio.INPUT)
        self.pi.set_pull_up_down(self.echo, pigpio.PUD_DOWN)
        self.cb1 = pi.callback(echo, pigpio.RISING_EDGE, self.cbf)

    def cbf(gpio, level, tick):
        rising = tick
        print(rising)
        return
 
if __name__ == '__main__':
    print "started"
    sonar = Sonar(16)