#!/usr/bin/python3
# -*- coding: utf-8 -*-
import rospy
from yh_dual.msg import YhDual

def msgCallback(msg):
    rospy.loginfo(f"{msg.stamp.secs}.{msg.stamp.nsecs}")

def yh_dual_time():
    rospy.init_node("yh_dual_time")
    rospy.Subscriber("yh_dual_topic", YhDual, msgCallback, queue_size=10)
    rospy.spin()

if __name__ == "__main__":
    yh_dual_time()