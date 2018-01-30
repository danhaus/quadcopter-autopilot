#!/usr/bin/env python
import rospy
import sys
import subprocess
import time

from roslib import message
from std_msgs.msg import String
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.point_cloud2 import PointCloud2

pts = 1
key_points = []

def kinect_callback(data):
    height = int (data.height)
    middle_x = int (data.width)
    depth = get_depth(middle_x, height, data)


def get_depth(width, height, data):
    #print("width: %f", data.width);
    #print("height: %f", data.height);
    global pts, key_points

    #data_out = pc2.read_points(data, field_names=None, skip_nans=True) # get all of the points
    data_out = pc2.read_points(data, field_names = {"z"}, skip_nans=False, uvs=key_points)
    if pts == 1:
        print("---points---")
        depth_threshold = 1.0
        filter_value = .01
        cluster = 1
        for point in data_out:
            if str(point[0]) == "nan" or point[0] <= depth_threshold:
                print("STOP")
            else:
                print(point[0]);
        pts = 1
        return 0


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/camera/depth_registered/points", PointCloud2, kinect_callback)
    rospy.spin()


def cleanup():
    print("whatup")


def start_roscore():
    command = "roscore"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    print(process.pid)
    time.sleep(4)


def start_kinect():
    command = "roslaunch freenect_launch freenect.launch"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    print(process.pid)
    time.sleep(4)


if __name__ == '__main__':
    #cleanup()
    #start_roscore()
    #start_kinect()

    min_x = 80
    max_x = 560
    min_y = 80
    max_y = 400

    current_x = min_x
    current_y = min_y

    while current_y <= max_y:
        current_x = min_x
        while current_x <= max_x:
            key_points.append([current_x, current_y])
            current_x += 80
        
        current_y += 80

    key_points = key_points.reverse()
 

    listener()
