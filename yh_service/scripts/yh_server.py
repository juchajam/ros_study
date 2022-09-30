#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
from yh_service.srv import YhSrv, YhSrvResponse

def multiply(req):
    res = YhSrvResponse()
    res.result = req.a * req.b
    rospy.loginfo(f"a:{req.a}, b:{req.b}, result:{res.result}")
    return res

def multiply_server():
    rospy.init_node("yh_server")
    yh_server = rospy.Service("multiply", YhSrv, multiply)
    rospy.loginfo("Server Ready")
    rospy.spin()

if __name__ == "__main__":
    multiply_server()