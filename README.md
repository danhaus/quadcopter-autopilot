# Quadcopter with autopilot: propelled_cow

Quadcopter contains a grabber capable of lifting a payload from the ground. Autonomous mode grabs a payload, then takes off and hovers at 80 cm above the ground. When the quadcopter is in stable flight, it drops its load and continues hovering. Autopilot is written in Python 2.7 with ROS framework.

![overview](img/overview.jpg?raw=true "wiring diagram")
![bottom](img/bottom.jpg?raw=true "wiring diagram")
![grabber](img/grabber.jpg?raw=true "wiring diagram")

## Autopilot description
 - Parameters for flight are set in src/hyper_propelled_cow/launch/parameters/default.yaml
 - After starting the autopilot (described below), motors start spinning with given power and their speed is continuously increasing until the quadcopter takes off.
 - PWM limits for controlling the motors are set based on the current PWM value.
 - PID controller is enabled: it inputs distance from the ground and outputs PWM value for the motors.
 - Distance from the ground comes from two sources: ultrasonic sensor and sonar. Both are usually quite noisy, so the following processing is performed:
 - Raw reading is saturated between 1 and 3000 mm to eliminate anomalous data.
 - A median filter is applied to further reduce the noise.
 - Both readings are fed to sensor fusion algorithm (src/hyper_propelled_cow/scripts/sensor_fuser)
 - This algorithm determines consistency of both readings and publishes the more consistent one.
 - It is also capable of determining a failure of a sensor. If both sensors stop responding, it switches into fail-safe mode and lands the quadcopter.

## Electronics:
 - Raspberry Pi 3B (RPi)
 - Arduino Nano connected with a USB cable to the RPi
 - Flight controller Naze32
 - ultrasonic sensor HC-SR04 connected to the RPi through a potential divider
 - sonar MB1040 LV-MaxSonar-EZ4 connected to the Arduino
 - receiver
 - relay switching between remote control and autopilot (toggled from a remote controller)

![wiring diagram](img/wiring_diagram.png?raw=true "wiring diagram")
