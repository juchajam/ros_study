#!/usr/bin/python
# -*- coding: utf-8 -*-
import rospy
# from std_msgs.msg import Int32
from msg_tutorial.msg import Mymsg

def msg_talker():
    rospy.init_node("py_msg_pub")

    pub = rospy.Publisher("burger", Mymsg, queue_size=10)

    loop_rate = rospy.Rate(5)

    msg = Mymsg()
    cnt = 0

    while not rospy.is_shutdown():
        # Mymsg:
        #   time stamp
        #   int32 data
        msg.stamp = rospy.Time.now()
        msg.data = cnt
        rospy.loginfo("send msg : %d", msg.stamp.secs)
        rospy.loginfo("send msg : %d", msg.stamp.nsecs)
        rospy.loginfo("send msg : %d", msg.data)
        pub.publish(msg)
        cnt += 1
        loop_rate.sleep()

if __name__ == "__main__":
    try:
        msg_talker()
    except rospy.ROSInterruptException:
        pass
