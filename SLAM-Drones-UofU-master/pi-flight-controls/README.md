#Running the Quadcopter

Run python in interactive mode and then do the following:
```python
from ctrl import fc

controller = fc()
#Start up countdown
controller.setThrottle(2000)
#Now at max throttle
controller.setThrottle(1000)
#Now at minimum throttle
controller.setRoll(1500)
#And so on...
controller.setPitch(1500)
controller.setYaw(1500)
```

#Attitude Values

To see the attitude values of the IMU run `python attitude.py`

#Ultrasonic

You can just run `python ultrasonic.py` to see the difference real quick, or you can make an object for use in other code.
```python
from ultrasonic import distance

d = distance()
distance_value = d.distance()
#distance_value now contains the distance in centimeters
d.cleanup(None, None)
#Or just press ctrl + c to cleanup.
```