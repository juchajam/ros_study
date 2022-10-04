#!/usr/bin/python3
# -*- coding: utf-8 -*-
import rospy
from yh_difference.srv import YhDifference, YhDifferenceResponse

def difference(req):
    res = YhDifferenceResponse()
    res.result = abs(req.a - req.b)
    return res

def difference_server():
    rospy.init_node("yh_difference_server")
    rospy.Service("yh_difference_service", YhDifference, difference)
    rospy.spin()

if __name__ == "__main__":
    difference_server()