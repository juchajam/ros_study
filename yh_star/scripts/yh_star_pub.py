#!/usr/bin/python3
# -*- coding: utf-8 -*-
import rospy
from yh_star.msg import YhStarMsg

def star_publisher():
    rospy.init_node("yh_star_pub")
    pub = rospy.Publisher("yh_star_topic", YhStarMsg, queue_size=10)

    loop_rate = rospy.Rate(2)

    msg = YhStarMsg()
    msg.data = 1

    while not rospy.is_shutdown():
        msg.stamp = rospy.Time.now()
        pub.publish(msg)
        msg.data += 1
        loop_rate.sleep()

if __name__ == "__main__":
    star_publisher()