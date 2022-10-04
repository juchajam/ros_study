#include "ros/ros.h"
#include "yh_dual/YhDual.h"

void msgCallback(const yh_dual::YhDual::ConstPtr& msg)
{
    ROS_INFO("%d", msg->data);
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "yh_dual_int");
    ros::NodeHandle nh;

    ros::Subscriber sub = nh.subscribe("yh_dual_topic", 100, msgCallback);

    ros::spin();

    return 0;
}