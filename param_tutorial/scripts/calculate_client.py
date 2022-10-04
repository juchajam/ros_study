#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
from param_tutorial.srv import Calculate, CalculateRequest
import sys

def calculate_client():
    rospy.init_node("calculate_client")

    if len(sys.argv) != 3:
        rospy.loginfo("rosrun param_tutorial calculate_client.py a b")
        rospy.loginfo("a, b: int32 number")
        sys.exit(1)

    my_client = rospy.ServiceProxy("calculate", Calculate)

    req = CalculateRequest()
    req.a = int(sys.argv[1])
    req.b = int(sys.argv[2])

    try:
        res = my_client(req)
        rospy.loginfo(f"a: {req.a}, b: {req.b}, result: {res.result}")
    except rospy.ServiceException as e:
        rospy.logerr(f"Failed : {e}")
        sys.exit(1)

if __name__ == "__main__":
    calculate_client()

