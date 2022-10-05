#include "ros/ros.h"
#include "std_msgs/Int32.h"

int main(int argc, char** argv)
{
    ros::init(argc, argv, "yh_connect_pub");
    ros::NodeHandle nh;

    ros::Publisher pub = nh.advertise<std_msgs::Int32>("yh_connect_int", 10);
    
    ros::Rate loop_rate(4);
    std_msgs::Int32 msg;

    while (ros::ok())
    {
        pub.publish(msg);
        msg.data++;
        loop_rate.sleep();
    }

    return 0;
}