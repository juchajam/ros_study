#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
from yh_check.msg import YhCheck

class MyCheck:
    def __init__(self):
        self.sub_distance = rospy.Subscriber("check_distance", YhCheck, self.distanceCallback)
        self.sub_camera = rospy.Subscriber("check_camera", YhCheck, self.cameraCallback)
        self.distance = True
        self.camera = True
    
    def distanceCallback(self, msg):
        self.distance = msg.data
        if self.distance and self.camera:
            rospy.loginfo("Ok")

    def cameraCallback(self, msg):
        self.camera = msg.data
        if self.distance and self.camera:
            rospy.loginfo("Ok")

if __name__ == "__main__":
    rospy.init_node("yh_check_sub")
    my_check = MyCheck()
    rospy.spin()
