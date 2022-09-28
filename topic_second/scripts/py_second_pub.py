#!/usr/bin/python
# -*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Int32

def my_counter():
    rospy.init_node("py_second_pub")
    pub = rospy.Publisher("my_count", Int32, queue_size=100)

    loop_rate = rospy.Rate(20)

    msg = Int32()
    msg.data = 0

    while not rospy.is_shutdown():
        pub.publish(msg)
        loop_rate.sleep()
        msg.data += 1

if __name__ == "__main__":
    try:
        my_counter()
    except rospy.ROSInterruptException:
        pass