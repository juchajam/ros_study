#include "ros/ros.h"
#include "yh_service/YhSrv.h"
#include <cstdlib>

int main(int argc, char** argv)
{
    ros::init(argc, argv, "yh_client");

    // {"yh_client", "a", "b"}
    if (argc != 3)
    {
        ROS_INFO("rosrun yh_service yh_client a b");
        ROS_INFO("a, b: int32 number");
        return 1;
    }

    ros::NodeHandle nh;

    ros::ServiceClient yh_client = nh.serviceClient<yh_service::YhSrv>("multiply");

    yh_service::YhSrv srv;
    srv.request.a = atoi(argv[1]);
    srv.request.b = atoi(argv[2]);

    if (yh_client.call(srv))
    {
        ROS_INFO("a:%d, b:%d", srv.request.a, srv.request.b);
        ROS_INFO("result: %d", srv.response.result);
    }
    else
    {
        ROS_ERROR("Failed to call service");
        return 1;
    }

    return 0;
}
