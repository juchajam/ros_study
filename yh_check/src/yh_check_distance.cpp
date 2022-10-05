#include "ros/ros.h"
#include "yh_check/YhCheck.h"

int main(int argc, char** argv)
{
    ros::init(argc, argv, "yh_check_distance");
    ros::NodeHandle nh;

    ros::Publisher pub = nh.advertise<yh_check::YhCheck>("check_distance", 10);
    ros::Rate loop_rate(2);

    yh_check::YhCheck msg;
    msg.data = true;

    while (ros::ok())
    {
        msg.stamp = ros::Time::now();
        pub.publish(msg);
        msg.data = !msg.data;
        loop_rate.sleep();
    }

    return 0;
}