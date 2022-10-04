#!/usr/bin/python3
# -*- coding: utf-8 -*-
import rospy
from yh_dual.msg import YhDual

def yh_dual_pub():
    rospy.init_node("yh_dual_pub")
    pub = rospy.Publisher("yh_dual_topic", YhDual, queue_size=10)
    loop_rate = rospy.Rate(8)
    msg = YhDual()

    while not rospy.is_shutdown():
        msg.stamp = rospy.Time.now()
        pub.publish(msg)
        msg.data += 1
        loop_rate.sleep()

if __name__ == "__main__":
    try:
        yh_dual_pub()
    except rospy.ROSInterruptException:
        pass