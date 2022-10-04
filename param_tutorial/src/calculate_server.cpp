#include "ros/ros.h"
#include "param_tutorial/Calculate.h"

#define PLUS 1
#define MINUS 2
#define MULTIPLICATION 3
#define DIVISION 4

int my_operator = PLUS;

bool calculation(param_tutorial::Calculate::Request& req,
                param_tutorial::Calculate::Response& res)
{
    switch (my_operator)
    {
        case PLUS:
            res.result = req.a + req.b;
            break;
        case MINUS:
            res.result = req.a - req.b;
            break;
        case MULTIPLICATION:
            res.result = req.a * req.b;
            break;
        case DIVISION:
            res.result = req.a / req.b;
            break;
        default:
            res.result = req.a + req.b;
            break;
    }
    ROS_INFO("a: %d, b: %d, result: %d", req.a, req.b, res.result);
    return true;
}

int main(int argc, char** argv)
{
    ros::init(argc, argv, "calculate_server");
    ros::NodeHandle nh;

    nh.setParam("calculation_method", PLUS); // 파라미터 초기 설정

    ros::ServiceServer calculate_server = nh.advertiseService("calculate", calculation);

    ros::Rate loop_rate(10);
    while (ros::ok())
    {
        nh.getParam("calculation_method", my_operator);
        ros::spinOnce();
        loop_rate.sleep();
    }

    return 0;
}