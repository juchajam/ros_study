#include "ros/ros.h"
#include "param_tutorial/Calculate.h"
#include <cstdlib>

int main(int argc, char** argv)
{
    ros::init(argc, argv, "calculate_client");

    if (argc != 3)
    {
        ROS_INFO("rosrun param_tutorial calculate_client a b");
        ROS_INFO("a, b : int32 number");
        return 1;
    }

    ros::NodeHandle nh;

    ros::ServiceClient calculate_client = nh.serviceClient<param_tutorial::Calculate>("calculate");

    param_tutorial::Calculate srv;
    srv.request.a = atoi(argv[1]);
    srv.request.b = atoi(argv[2]);

    if (calculate_client.call(srv))
    {
        ROS_INFO("a : %d, b : %d, result : %d", srv.request.a, srv.request.b, srv.response.result);
    }
    else
    {
        ROS_ERROR("Failed to call service");
        return 1;
    }

    return 0;
}