#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist

rospy.init_node("turtle_patrol")
pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=50)

loop_rate = rospy.Rate(2)
msg = Twist()
msg.linear.x = 1.0

while not rospy.is_shutdown():
    pub.publish(msg)
    msg.linear.x *= -1
    loop_rate.sleep()
