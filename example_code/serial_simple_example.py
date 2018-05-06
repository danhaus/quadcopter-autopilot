import serial

# ser = serial.Serial('/dev/ttyACM0', 9600)
# ser = serial.Serial('/dev/ttyS0', 9600)
# ser = serial.Serial('/dev/ttyAMA0', 9600)
ser = serial.Serial('/dev/ttyUSB0', 9600)



while True:
	try:
		# print int(ser.readline().strip())
		print ser.readline()

	except ValueError:
		print "ValueError"