#!/usr/bin/env python

from kinect import Kinect

DEPTH_THRESHOLD=.5
RUNNING_TIME=120
TOPIC="/camera/depth_registered/points"

if __name__ == "__main__":
    kinect = Kinect(topic = TOPIC, min_depth = DEPTH_THRESHOLD, run_time = RUNNING_TIME)
