#include "ros/ros.h"
#include "std_msgs/Int32.h"
#include "std_msgs/Float32.h"

ros::Publisher pub;

void msgCallback(const std_msgs::Int32::ConstPtr& msg)
{
    if (msg->data % 5 == 0)
    {
        std_msgs::Float32 float_msg;
        float_msg.data = (float) msg->data / 3.0f;
        pub.publish(float_msg);
    }
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "yh_connect_sub_pub");
    ros::NodeHandle nh;

    ros::Subscriber sub = nh.subscribe("yh_connect_int", 10, msgCallback);
    pub = nh.advertise<std_msgs::Float32>("yh_connect_float", 10);

    ros::spin();

    return 0;
}