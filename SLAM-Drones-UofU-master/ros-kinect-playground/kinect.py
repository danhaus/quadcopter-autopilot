#!/usr/bin/env python
import rospy
import sys
import subprocess
import time, timeit
from quadcopter import Quadcopter
from roslib import message
from std_msgs.msg import String
import sensor_msgs.point_cloud2 as pc2
from sensor_msgs.point_cloud2 import PointCloud2


class Kinect:
    def __init__(self, topic="/camera/depth_registered/points", min_depth=.5, run_time=60):
        self.cleanup_ros()
        self.core = self.start_roscore()
        self.kinect = self.start_kinect()
        self.min_depth = min_depth
        self.run_time = run_time
        # self.rosbag = self.start_record()
        rospy.init_node('listener', anonymous=True)
        self.subscribed_topic = rospy.Subscriber(topic, PointCloud2, self.scanned)
        # build key points
        self.object_map = [[0 for x in range(4)] for y in range(8)]
        self.key_points = []
        min_x = 100
        max_x = 560
        min_y = 80
        max_y = 400
        current_y = max_y
        while current_y >= min_y:
            current_x = max_x
            while current_x >= min_x:
                self.key_points.append([current_x, current_y])
                current_x -= 80
            current_y -= 80
        # init quadcopter
        self.quadcopter = Quadcopter()
        # begin interrupt driven runtime
        self.start = timeit.default_timer()
        rospy.spin()

    def start_record(self):
        # TODO record
        command = ""
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        print("ROSBAG PID: " + str(process.pid))
        time.sleep(4)
        return process

    def start_roscore(self):
        command = "roscore"
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        print("ROSCORE PID: " + str(process.pid))
        time.sleep(4)
        return process

    def start_kinect(self):
        command = "roslaunch freenect_launch freenect-registered-xyzrgb.launch"
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        print("ROSLAUNCH PID: " + str(process.pid))
        time.sleep(4)
        return process

    def cleanup_ros(self):
        command = 'pkill "ros"'
        process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        time.sleep(4)

    def scanned(self, data):
        points = pc2.read_points(data, field_names={"z"}, skip_nans=False, uvs=self.key_points)
        locater = 0
        for point in points:
            row = locater / 8
            col = locater % 8

            point_depth = point[0]
            if str(point_depth) == "nan":
                point_depth = 0

            self.object_map[col][row] = point_depth

            locater += 1

        #print(self.object_map)
        time.sleep(1)
        self.interpret_data()

    def interpret_data(self):
        full_left = 0
        full_right = 0
        full_top = 0
        full_bottom = 0
        # Top Left
        points = [self.object_map[0][0], self.object_map[0][1], self.object_map[1][0], self.object_map[1][1]]
        avg = sum(points)/len(points)
        if avg < self.min_depth:
            full_left += 1
            full_top += 1
        # Top Mid Left
        points = [self.object_map[2][0], self.object_map[3][0], self.object_map[2][1], self.object_map[3][1]]
        avg = sum(points)/len(points)
        if avg < self.min_depth:
            full_left += 1
            full_top += 1
        # Top Mid Right
        points = [self.object_map[4][0], self.object_map[5][0], self.object_map[4][1], self.object_map[5][1]]
        avg = sum(points)/len(points)
        if avg < self.min_depth:
            full_right += 1
            full_top += 1
        # Top Right
        points = [self.object_map[6][0], self.object_map[7][0], self.object_map[6][1], self.object_map[7][1]]
        avg = sum(points)/len(points)
        if avg < self.min_depth:
            full_right += 1
            full_top += 1

        # Bot Left
        points = [self.object_map[0][2], self.object_map[0][3], self.object_map[1][2], self.object_map[1][3]]
        avg = sum(points)/len(points)
        if avg < self.min_depth:
            full_left += 1
            full_bottom += 1
        # Bot Mid Left
        points = [self.object_map[2][2], self.object_map[2][3], self.object_map[3][2], self.object_map[3][3]]
        avg = sum(points)/len(points)
        if avg < self.min_depth:
            full_left += 1
            full_bottom += 1
        # Bot Mid Right
        points = [self.object_map[4][2], self.object_map[5][2], self.object_map[4][3], self.object_map[5][3]]
        avg = sum(points)/len(points)
        if avg < self.min_depth:
            full_right += 1
            full_bottom += 1
        # Bot Right
        points = [self.object_map[6][2], self.object_map[7][2], self.object_map[6][3], self.object_map[7][3]]
        avg = sum(points)/len(points)
        if avg < self.min_depth:
            full_right += 1
            full_bottom += 1

        #i = 0
        #while i < len(self.object_map):
        #    e = 0
        #     while e < len(self.object_map[i]):
        #         if self.object_map[i][e] == 0 and (i != 6 or e != 3) and (i != 7 or e i!=3):
        #             print("Zero at " + str(i) + ", " + str(e))
        #         e += 1
        #     i += 1

        if full_right >= 4:
            print("Object on the Right")
            self.quadcopter.stop()
            self.quadcopter.rotate_left(90)
        if full_left >= 4:
            print("Object on the Left")
            self.quadcopter.stop()
            self.quadcopter.rotate_right(90)
        if full_bottom >= 4:
            print("Object on the Bottom")
            self.quadcopter.stop()
        if full_top >= 4:
            print("Object on the Top")
            self.quadcopter.stop()
        else:
            print("Move forward")

    def check_timer(self):
        end = timeit.default_timer() - self.start
        if end >= self.run_time:
            del self

    def __exit__(self):
        self.quadcopter.begin_dissent()
        self.core.kill()
        self.kinect.kill()
        # self.rosbag.kill()
        self.cleanup_ros()
        del self.quadcopter
