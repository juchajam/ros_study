#!/usr/bin/python3
# -*_ coding: utf-8 -*-

import rospy
from std_msgs.msg import Int32

class ConnectPub:
    def __init__(self):
        self.pub = rospy.Publisher("yh_connect_int", Int32)
        self.msg = Int32()
        self.loop_rate = rospy.Rate(4)

    def run(self):
        while not rospy.is_shutdown():
            self.pub.publish(self.msg)
            self.msg.data += 1
            self.loop_rate.sleep()

if __name__ == "__main__":
    rospy.init_node("yh_connect_pub")
    connect_pub = ConnectPub()
    connect_pub.run()
