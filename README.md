# Quadcopter autopilot

Autopilot is written in Python 2.7 with ROS framework. Quadcopter contains a grabber capable of lifting a payload from the ground. Autonomous mode grabs a payload, then takes off and hovers at 80 cm above the ground. When the quadcopter is in stable flight, it drops its load and continues hovering. Autopilot can be disabled any time from a remote controller, which enables manual control.

![overview](img/overview.jpg?raw=true "wiring diagram")
![bottom](img/bottom.jpg?raw=true "wiring diagram")
![grabber](img/grabber.jpg?raw=true "wiring diagram")

## Autopilot description
 - After starting the autopilot (described below), motors start spinning with given power and their speed is continuously increasing until the quadcopter takes off.
 - PWM limits for controlling the motors are set based on the current PWM value.
 - PID controller is enabled: it inputs distance from the ground and outputs PWM value for the motors.
 - Distance from the ground comes from two sources: ultrasonic sensor and sonar. Both are usually quite noisy, so the following processing is performed:
 - Raw reading is saturated between 1 and 3000 mm.
 - A median filter is applied to further reduce the noise.
 - Both readings are fed to sensor fusion algorithm (src/hyper_propelled_cow/scripts/sensor_fuser)
 - This algorithm determines consistency of both readings and chooses the smoother one.
 - Exponential smoothening is applied and then the distance is published to the PID controller.
 - The sensor fusion is also capable of determining a failure of a sensor. If both sensors stop responding, it switches into fail-safe mode and lands the quadcopter.
 - Quadcopter transmits live messages to laptop about its behaviour, e.g. when a sensor fails or a 10-second countdown before it takes off.

## Install
### Raspberry Pi (RPi)
On your RPi with Ubuntu / Lubuntu install ROS Kinetic: http://wiki.ros.org/kinetic/Installation/Ubuntu <br />
Clone this repo.
Then in terminal run:
```
sudo apt-get install pigpio python-pigpio
cd ~/quadcopter-autopilot
catkin_make
```
to install pigpio library for PWM interface and build the code in catkin workspace.
Upload src/Arduino code/main/main.ino to your Arduino and connect it with a USB cable to the RPi

## Usage
Parameters for flight are set in src/hyper_propelled_cow/launch/parameters/default.yaml <br />
On a laptop SSH to the RPi and run:
```
sudo pigpiod
roslaunch hyper_propelled_cow initialize.launch
```
to enable PWM communication and initialise the drone. Grabber closes now. <br />
To start recording all ROS messages to rosbag run in a new terminal
```
rosrun rosbag record -a
```
To start the autopilot, in a new terminal run
```
rosrun hyper_prolled_cow controller_dynamic
```
This starts 10-second countdown streamed to your terminal and then the drone takes off.
After it stabilises itself at given altitude, it drops the payload and continues hovering. To land, disable the autopilot from your remote and take over manual control.

## Electronics:
 - Raspberry Pi 3B (RPi)
 - Arduino Nano connected with a USB cable to the RPi
 - Flight controller Naze32
 - ultrasonic sensor HC-SR04 connected to the RPi through a potential divider
 - sonar MB1040 LV-MaxSonar-EZ4 connected to the Arduino
 - receiver
 - relay switching between remote control and autopilot (toggled from a remote controller)

![wiring diagram](img/wiring_diagram.png?raw=true "wiring diagram")
