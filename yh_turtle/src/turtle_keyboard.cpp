#include "ros/ros.h"
#include "geometry_msgs/Twist.h"

ros::Publisher pub;

void msgCallback(const geometry_msgs::Twist::ConstPtr& msg)
{
    pub.publish(*msg);
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "turtle_keyboard");
    ros::NodeHandle nh;

    pub = nh.advertise<geometry_msgs::Twist>("turtle1/cmd_vel", 100);
    ros::Subscriber sub = nh.subscribe("cmd_vel", 100, msgCallback);

    ros::spin();

    return 0;
}