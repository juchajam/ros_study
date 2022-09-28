#include "ros/ros.h"
#include "std_msgs/Int32.h"

int main(int argc, char** argv)
{
    ros::init(argc, argv, "second_pub");
    ros::NodeHandle nh;

    ros::Publisher pub = nh.advertise<std_msgs::Int32>("my_count", 100);

    ros::Rate loop_rate(2);

    std_msgs::Int32 msg;
    msg.data = 0;

    while (ros::ok())
    {
        pub.publish(msg);
        loop_rate.sleep();
        msg.data++;
    }

    return 0;
}