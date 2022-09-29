#!/usr/bin/python
# -*- coding: utf-8 -*-
import rospy
from service_tutorial.srv import AddTwoInts, AddTwoIntsResponse

def add(req):
    result = req.a + req.b
    rospy.loginfo("a=%d, b=%d", req.a, req.b)
    rospy.loginfo("response: result=%d", result)
    return AddTwoIntsResponse(result)

def add_two_ints_server():
    rospy.init_node("py_server")

    my_server = rospy.Service("add_two_ints", AddTwoInts, add)
    
    rospy.loginfo("Service Server Ready.")

    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
