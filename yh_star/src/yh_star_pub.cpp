#include "ros/ros.h"
#include "yh_star/YhStarMsg.h"

int main(int argc, char** argv)
{
    ros::init(argc, argv, "yh_star_pub");
    ros::NodeHandle nh;

    ros::Publisher pub = nh.advertise<yh_star::YhStarMsg>("yh_star_topic", 5);

    ros::Rate loop_rate(2);

    yh_star::YhStarMsg msg;
    msg.data = 1;

    while (ros::ok())
    {
        msg.stamp = ros::Time::now();
        pub.publish(msg);
        msg.data++;
        loop_rate.sleep();
    }

    return 0;
}