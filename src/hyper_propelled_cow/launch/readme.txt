how to launch

a) sudo pigpiod
b) roslaunch propelled_cow arming.launch
c) crtl-c after it has launched (it will start producing arming PWM to the throttle and keep it even after crt-c)
d) roslaunch propelled_cow initilize.launch (initilise all the function apart controlling logic - the drone will not fly)
e) in a new terminal: roslaunch propelled_cow fly_to_the_sky.launch