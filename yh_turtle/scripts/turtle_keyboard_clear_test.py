#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty

class TurtleKeyboardClearTest:
    def __init__(self):
        self.sub = rospy.Subscriber("cmd_vel", Twist, self.msgCallback)
        self.pub = rospy.Publisher("turtle1/cmd_vel", Twist, queue_size=100)
        self.clear_client = rospy.ServiceProxy("clear", Empty)

    def msgCallback(self, msg):
        if msg.linear.z > 0.0:
            self.call()
        else:
            self.pub.publish(msg)

    def call(self):
        try:
            self.clear_client()
        except rospy.ServiceException as e:
            rospy.logerr(f"Failed : {e}")

if __name__ == "__main__":
    rospy.init_node("turtle_keyboard_clear_test")
    turtle_keyboard_clear_test = TurtleKeyboardClearTest()
    rospy.spin()
