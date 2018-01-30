import time
import csv
from ctrl import fc

sleep_time = .05
f = fc()

with open('flight-data.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        f.setRoll(int(row[0]))
        f.setPitch(int(row[1]))
        f.setYaw(int(row[2]))
        f.setThrottle(int(row[3]))
        time.sleep(sleep_time)
