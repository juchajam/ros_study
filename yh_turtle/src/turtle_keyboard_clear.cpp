#include "ros/ros.h"
#include "geometry_msgs/Twist.h"
#include "std_srvs/Empty.h"

ros::Publisher pub;
ros::ServiceClient clear_client;
std_srvs::Empty srv;

void msgCallback(const geometry_msgs::Twist::ConstPtr& msg)
{
    if (msg->linear.z > 0.0)
    {
        if (clear_client.call(srv))
        {
            ROS_INFO("CLEAR");
        }
        else
        {
            ROS_ERROR("FAILED");
        }
    }
    else
    {
        pub.publish(*msg);
    }
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "turtle_keyboard_clear");
    ros::NodeHandle nh;

    pub = nh.advertise<geometry_msgs::Twist>("turtle1/cmd_vel", 100);
    clear_client = nh.serviceClient<std_srvs::Empty>("clear");
    ros::Subscriber sub = nh.subscribe("cmd_vel", 100, msgCallback);

    ros::spin();

    return 0;
}