import serial
import time

# ser = serial.Serial('/dev/ttyACM0', 9600)
ser = serial.Serial('/dev/ttyS0', 9600)
# ser = serial.Serial('/dev/ttyAMA0', 9600)

# ser = serial.Serial('/dev/ttyUSB0', 9600)

last_received=''
serbuffer = ''

while 1:
    # time.sleep(5)
    serbuffer += ser.read(ser.inWaiting())
    if '\n' in serbuffer:
        lines = serbuffer.split('\n') # Guaranteed to have at least 2 entries
        last_received = lines[-2]
        serbuffer = lines[-1]
    print('Reading [mm]: ' + str(last_received))
    # time.sleep(25)