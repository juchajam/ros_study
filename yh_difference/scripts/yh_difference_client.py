#!/usr/bin/python3
# -*- coding: utf-8 -*-
from pydoc import cli
import rospy
from yh_difference.srv import YhDifference, YhDifferenceRequest
import sys

def difference_client():
    rospy.init_node("yh_difference_client")
    
    if len(sys.argv) != 3:
        rospy.loginfo("rosrun yh_difference yh_difference_client.py a b")
        rospy.loginfo("a, b: int32 number")
        sys.exit(1)

    client = rospy.ServiceProxy("yh_difference_service", YhDifference)
    req = YhDifferenceRequest()
    req.a = int(sys.argv[1])
    req.b = int(sys.argv[2])

    try:
        res = client(req)
        rospy.loginfo(res.result)
    except rospy.ServiceException:
        rospy.logerr("Failed")
        sys.exit(1)

if __name__ == "__main__":
    difference_client()