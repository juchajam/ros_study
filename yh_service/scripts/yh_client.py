#!/usr/bin/python3
# -*- coding: utf-8 -*-

from audioop import mul
import rospy
from yh_service.srv import YhSrv, YhSrvRequest
import sys

def multiply_client():
    rospy.init_node("yh_client")

    if len(sys.argv) != 3:
        rospy.loginfo("rosrun yh_service yh_client.py a b")
        rospy.loginfo("a, b: int32 number")
        sys.exit(1)
    
    yh_client = rospy.ServiceProxy("multiply", YhSrv)

    req = YhSrvRequest()
    req.a = int(sys.argv[1])
    req.b = int(sys.argv[2])

    try:
        res = yh_client(req)
        rospy.loginfo(f"a: {req.a}, b: {req.b}, result: {res.result}")
    except rospy.ServiceException as e:
        rospy.logerr(f"Fail: {e}")


if __name__ == "__main__":
    multiply_client()
    