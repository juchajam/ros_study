#include "ros/ros.h"
#include "std_msgs/Int32.h"
#include "std_msgs/Float32.h"

class ConnectSubPub
{
    public:
        ConnectSubPub()
        {
            sub = nh.subscribe("yh_connect_int", 10, &ConnectSubPub::msgCallback, this);
            pub = nh.advertise<std_msgs::Float32>("yh_connect_float", 10);
        }
        void msgCallback(const std_msgs::Int32::ConstPtr& msg)
        {
            if (msg->data % 5 == 0)
            {
                float_msg.data = (float) msg->data / 3.0f;
                pub.publish(float_msg);
            }
        }
    private:
        ros::NodeHandle nh;
        ros::Publisher pub;
        ros::Subscriber sub;
        std_msgs::Float32 float_msg;
}; 

int main(int argc, char** argv)
{
    ros::init(argc, argv, "yh_connect_sub_pub_class");
    ConnectSubPub connect_sub_pub = ConnectSubPub();
    ros::spin();
    return 0;
}