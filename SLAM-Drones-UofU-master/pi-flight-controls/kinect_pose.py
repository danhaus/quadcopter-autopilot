#!/usr/bin/env python
from ctrl import fc
import math
import rospy
import sys
import subprocess
import time, timeit
from roslib import message
from std_msgs.msg import String
from nav_msgs.msg import Odometry

'''
Kinect Axses from https://msdn.microsoft.com/en-us/library/hh973078.aspx:

 |z
 |
 |_ _ _ _ _y
 \
  \
   \x

ASSUMING: x = PITCH
          y = ROLL
          z = THROTTLE

'''

class Kinect_Odom:

    def __init__(self, flight_controller):
        self.flight_controller = flight_controller
        self.dx = 0
        self.dx_dt = 0
        self.pose_x = 0
        self.dy = 0
        self.dy_dt = 0
        self.pose_y = 0
        self.pose1_x = 0
        self.pose2_x = 0
        self.pose1_y = 0
        self.pose2_y = 0
        self.pose1_z = 0
        self.pose2_z = 0
        self.dz = 0
        self.dz_dt = 0
        self.pose_z = 0
        self.dt_sec = 0
        self.dt_nsec = 0
        self.t1_sec = 0
        self.t1_nsec = 0
        self.t2_sec = 0
        self.t2_nsec = 0
        self.pitch_trim = self.flight_controller.data[1]
        self.roll_trim = self.flight_controller.data[0]
        self.correction_p = .1
        self.correction_d = 0
        self.correction_max = 10
        self.correction_min = -10
        self.pitch_correction = 0
        self.roll_correction = 0

    def process_odom(self, odom_data):
        frame_sec = odom_data.header.stamp.secs
        frame_nsec = odom_data.header.stamp.nsecs
        self.pose_x = odom_data.pose.pose.position.x
        self.pose_y = odom_data.pose.pose.position.y
        self.pose_z = odom_data.pose.pose.position.z

        #calc dt:
        self.t1_sec = self.t2_sec
        self.t1_nsec = self.t2_nsec
        self.t2_sec = frame_sec
        self.t2_nsec = frame_nsec
        self.dt_sec = self.t2_sec - self.t1_sec
        self.dt_nsec = self.t2_nsec - self.t1_nsec

        #calc dx/dt for PITCH CORRECTION(m/nsec):
        self.pose1_x = self.pose2_x
        self.pose2_x = self.pose_x
        self.dx = self.pose2_x - self.pose1_x
        self.dx_dt = self.dx / (self.dt_sec*math.pow(10, 9) + self.dt_nsec)
        self.dx_dt *= math.pow(10, 9)*100
        #print("dx/dt (PITCH): " + str(self.dx_dt) + "\n")
        #TODO positive dx_dt means drif to the FRONT, PITCH PWM--
        #TODO negative dx_dt means drift to the BACK, PITCH PWM++
        #get current pitch
        pitch_correction = -(self.pose_x*correction_p + self.dx_dt*correction_d)
        if pitch_correction > correction_max:
            pitch_correction = correction_max
        elif pitch_correction < correction_min:
            pitch_correction = correction_min
        #f.setPitch()
        #self.flight_controller.setPitch(int(self.pitch_trim + pitch_correction))
        self.pitch_correction = pitch_correction

        #calc dy/dt for ROLL CORRECTION(m/nsec):
        self.pose1_y = self.pose2_y
        self.pose2_y = self.pose_y
        self.dy = self.pose2_y - self.pose1_y
        self.dy_dt = self.dy / (self.dt_sec*math.pow(10, 9) + self.dt_nsec)
        self.dy_dt *= math.pow(10, 9)*100
        #print("dy/dt (ROLL): " +  str(self.dy_dt) + "\n")
        #TODO positive dy_dt means drift RIGHT, ROLL PWM--
        #TODO negative dy_dt means drift LEFT, ROLL PWM++
        roll_correction = -(pose_y*correction_p + self.dy_dt*correction_d)
        if roll_correction > correction_max:
            roll_correction = correction_max
        elif roll_correction < correction_min:
            roll_correction = correction_min
        #f.setRoll()
        #self.flight_controller.setRoll(int(self.roll_trim + roll_correction))
        self.roll_correction = roll_correction

        '''
        Z axis taken care of by Ultrasonic:

        #calc dz/dt for THROTTLE CORRECTION(m/nsec):
        self.pose1_z = self.pose2_z
        self.pose2_z = self.pose_z
        self.dz = self.pose2_z - self.pose1_z
        self.dz_dt = self.dz / (self.dt_sec*math.pow(10,9) + self.dt_nsec)
        self.dz_dt *= math.pow(10, 9)*100
        #print("dz/dt (THROTTLE): "  + str(self.dz_dt) + "\n")
        #TODO positive dz_dt means drift (FORWARD / BACKWARD)
        #TODO negative dz_dt means drift (FORWARD / BACKWARD)
        #f.setPitch()'''

    def listener(self):
        rospy.init_node('estimated_trajectory_listener', anonymous=True)
        rospy.Subscriber('rtabmap/odom', Odometry, self.process_odom)
        rospy.spin()

    def reinit_position(self):
        self.pose1_x = 0
        self.pose2_x = 0
        self.dx = 0
        self.dx_dt = 0 #cm/sec
        self.pose1_y = 0
        self.pose2_y = 0
        self.dy = 0
        self.dy_dt = 0 #cm/sec
        self.pose1_z = 0
        self.pose2_z = 0
        self.dz = 0
        self.dz_dt = 0


if __name__ == '__main__':
    odom = Kinect_Odom()
    odom.listener()
