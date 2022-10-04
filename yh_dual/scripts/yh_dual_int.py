#!/usr/bin/python3
# -*- coding: utf-8 -*-
import rospy
from yh_dual.msg import YhDual

def msgCallback(msg):
    rospy.loginfo(msg.data)

def yh_dual_int():
    rospy.init_node("yh_dual_int")
    rospy.Subscriber("yh_dual_topic", YhDual, msgCallback, queue_size=10)
    rospy.spin()

if __name__ == "__main__":
    yh_dual_int()