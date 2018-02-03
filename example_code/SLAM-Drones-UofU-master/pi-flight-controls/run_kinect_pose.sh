#!/bin/bash
source /opt/ros/kinetic/setup.bash

#export ROS_MASTER_URI=http://192.168.1.253:11311
#export ROS_MASTER_URI=http://127.0.0.1:11311
export ROS_MASTER_URI=http://192.168.2.100:11311
#export ROS_MASTER_URI=http://dubuntu14:11311
#export ROS_IP=192.168.2.100
#export ROS_IP=192.168.1.8
export ROS_IP=$(hostname -i)
export PYTHONPATH="$PYTHONPATH:$ROS_ROOT/core/roslib/src"

python kinect_pose.py
