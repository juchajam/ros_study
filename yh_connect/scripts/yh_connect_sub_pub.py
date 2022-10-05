#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int32, Float32

class ConnectSubPub:
    def __init__(self):
        self.sub = rospy.Subscriber("yh_connect_int", Int32, self.msgCallback)
        self.pub = rospy.Publisher("yh_connect_float", Float32)
        self.float_msg = Float32()

    def msgCallback(self, msg):
        if msg.data % 5 == 0:
            self.float_msg.data = msg.data / 3
            self.pub.publish(self.float_msg)

if __name__ == "__main__":
    rospy.init_node("yh_connect_sub_pub")
    connect_sub_pub = ConnectSubPub()
    rospy.spin()
