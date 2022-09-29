#include "ros/ros.h"
#include "service_tutorial/AddTwoInts.h" // 서비스 헤더 파일
                                        // 빌드시 생성
#include <cstdlib> // atoi 함수 사용을 위한 라이브러리

int main(int argc, char** argv)
{
    ros::init(argc, argv, "my_client");

    // rosrun 패키지이름 노드이름 a b
    // argv = {노드이름, a, b}
    if (argc != 3) // 입력 오류 처리
    {
        ROS_INFO("command: rosrun service_tutorial my_client arg1 arg2");
        ROS_INFO("arg1, arg2 : int32 number");
        return 1;
    }

    ros::NodeHandle nh;

    // 서비스 클라이언트 (my_client)를 선언한다.
    // 서비스 이름은 (add_two_ints)이고 패키지 (service_tutorial)의 (AddTwoInts) 서비스 파일을 사용한다.
    ros::ServiceClient my_client = nh.serviceClient<service_tutorial::AddTwoInts>("add_two_ints");

    service_tutorial::AddTwoInts srv;

    // 노드 실행시 입력된 변수를 서비스 요청 값의 a, b에 저장한다.
    srv.request.a = atoi(argv[1]);
    srv.request.b = atoi(argv[2]);

    // 서비스를 요청하고, 응답이 정상적으로 왔을 경우, 값을 출력한다.
    if (my_client.call(srv))
    {
        ROS_INFO("send srv: srv.request.a=%d, srv.request.b=%d", srv.request.a, srv.request.b);
        ROS_INFO("receive srv: srv.response.result=%d", srv.response.result);
    }
    else
    {
        ROS_ERROR("Failed to call service");
        return 1;
    }


    return 0;
}