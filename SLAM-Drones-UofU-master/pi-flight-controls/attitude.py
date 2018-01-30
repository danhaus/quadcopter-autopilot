from pyMultiwii import MultiWii
from time import sleep
from sys import stdout

if __name__ == "__main__":

    board = MultiWii("/dev/ttyUSB0")
    board.disarm()

    while(True):
        board.getData(MultiWii.ATTITUDE)
        message = "angx = {:+.2f} \t angy = {:+.2f} \t heading = {:+.2f} \t elapsed = {:+.4f} \t".format(float(board.attitude['angx']),float(board.attitude['angy']),float(board.attitude['heading']),float(board.attitude['elapsed']))
        stdout.write("\r%s" % message )
        stdout.flush()
        sleep(0.03)
