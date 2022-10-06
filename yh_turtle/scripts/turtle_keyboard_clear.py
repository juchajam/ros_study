#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist
from std_srvs.srv import Empty
from turtle_keyboard import TurtleKeyboard
from turtle_clear import TurtleClear

class TurtleKeyboardClear(TurtleKeyboard, TurtleClear):
    def __init__(self):
        TurtleKeyboard.__init__(self)
        TurtleClear.__init__(self)

    def msgCallback(self, msg):
        if msg.linear.z > 0.0:
            self.call()
        else:
            self.pub.publish(msg)

if __name__ == "__main__":
    rospy.init_node("turtle_keyboard_clear")
    turtle_keyboard_clear = TurtleKeyboardClear()
    rospy.spin()
