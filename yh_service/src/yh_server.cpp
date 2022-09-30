#include "ros/ros.h"
#include "yh_service/YhSrv.h"

bool multiply(yh_service::YhSrv::Request& req,
            yh_service::YhSrv::Response& res)
{
    res.result = req.a * req.b;
    ROS_INFO("a:%d, b:%d, result=%d", req.a, req.b, res.result);
    return true;
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "yh_server");
    ros::NodeHandle nh;

    ros::ServiceServer yh_server = nh.advertiseService("multiply", multiply);

    ros::spin();

    return 0;
}