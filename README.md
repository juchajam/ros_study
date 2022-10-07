# ros_study
my first ros study

# [turtlesim 연습문제](./yh_turtle/turtlesim%20%EC%97%B0%EC%8A%B5%EB%AC%B8%EC%A0%9C.pdf)

## 2022년 9월 27일 시작
### [topic_tutorial](./topic_tutorial)
- topic_tutorial 패키지 생성
- my_publisher, my_subscriber 노드 생성
- 빌드
- 실행

## 2022년 9월 28일
### [topic_tutorial](./topic_tutorial)
- topic_tutorial 패키지에 python scripts 추가
- py_publisher.py, py_subscriber.py 노드 생성
- 빌드
- 실행

### [topic_second](./topic_second)
- topic_second 패키지 생성
- second_pub, second_sub, py_second_pub.py, py_second_sub.py 노드 생성
- 빌드
- 실행

### [과제1: topic_test](./topic_test)

## 2022년 9월 29일
### [msg_tutorial](./msg_tutorial)
- msg_tutorial 패키지 생성
- msg 디렉토리에 Mymsg.msg 생성
- msg_publisher, msg_subscsriber, py_msg_pub.py, py_msg_sub.py 노드 생성
- 빌드
- 실행

### [service_tutorial](./service_tutorial)
- service_tutorial 패키지 생성
- srv 디렉토리에 AddTwoInts.srv 생성
- my_server, my_client, py_server.py, py_client.py 노드 생성
- 빌드
- 실행

## 2022년 9월 30일
### [과제2: yh_star](./yh_star)
- for문 활용해서 별 찍기
    - yh_star 패키지 생성
    - yh_star_pub, yh_star_sub, yh_star_pub.py, yh_star_sub.py 노드 생성
    - 빌드
    - 실행

### [과제3: yh_service](./yh_service)
- yh_service 패키지 생성
- yh_server, yh_client, yh_server.py, yh_client.py 노드 생성
- 빌드
- 실행

## 2022년 10월 4일
### [param_tutorial](./param_tutorial)
- param_tutorial 패키지 생성
- calculate_server, calculate_client, calculate_server.py, calculate_client.py 노드 생성
- 빌드
- 실행
- [파라미터 서버 활용](#parameter-server)

### [과제4 yh_dual](./yh_dual)
- [과제4.pdf](./yh_dual/과제4.pdf)

### [과제5 yh_difference](./yh_difference)
- [과제5.pdf](./yh_difference/과제5.pdf)

## 2022년 10월 5일
### [과제6 yh_check](./yh_check)
- [과제6](./yh_check/과제6.pdf)
    - yh_check 패키지 생성
    - yh_check_distance, yh_check_camera, yh_check_sub, yh_check_distance.py, yh_check_camera.py, yh_check_sub.py 노드 생성
    - 빌드
    - 실행
    - Python 클래스로 작성

### [과제7 yh_connect](./yh_connect)
- [과제7](./yh_connect/과제7.pdf)
    - yh_connect 패키지 생성
    - yh_connect_pub, yh_connect_sub, yh_connect_sub_pub, yh_connect_pub.py, yh_connect_sub.py, yh_connect_sub_pub.py 노드 생성
    - 빌드
    - 실행
    - Python 클래스로 작성


## 2022년 10월 6일
### [yh_turtle](./yh_turtle)
- yh_turtle 패키지 생성
- turtle_patrol, turtle_keyboard, turtle_clear, turtle_keyboard_clear, turtle_patrol.py, turtle_keyboard.py, turtle_clear.py, turtle_keyboard_clear.py 노드 생성
- [teleop_twist_keyboard 패키지 설치](#teleop_twist_keyboard)
- 빌드
- 실행

### [roslaunch 실습](#roslaunch)

---

## ROS 명령어
### roscore
- ROS Master를 실행한다.
- 노드를 켜기 전에 가장 먼저 실행
```bash
juchajam@ubuntu:~$ roscore
```

### rosrun
- 노드를 실행한다.
- rosrun 패키지이름 노드이름
```bash
juchajam@ubuntu:~$ rosrun <패키지이름> <노드이름>
```

### catkin_create_pkg
- 현재 위치한 작업 공간에 패키지를 생성한다.
- catkin_create_pkg 패키지이름 의존성
```bash
juchajam@ubuntu:~$ catkin_create_pkg <패키지이름> [의존성1] [의존성2] .... 
```
ex)
```bash
juchajam@ubuntu:~$ catkin_create_pkg topic_tutorial roscpp rospy std_msgs
```

### Python3 설치 방법
- python3 설치
```bash
juchajam@ubuntu:~$ sudo apt install python3-pip python3-all-dev python3-rospkg
juchajam@ubuntu:~$ sudo apt install ros-melodic-desktop-full --fix-missing
```

### Parameter Server
- ROS Master에서 실행되고, 변수들을 담고 있는 서버
- ros::setParam(), ros::getParam(), rospy.set_param(), rospy.get_param() 등의 함수로 사용
- command line에서 rosparam으로 사용 가능
- rosparam list
    - 파라미터 서버의 모든 파라미터를 출력
```bash
juchajam@ubuntu:~$ rosparam list
```
- rosparam get <파라미터 이름>
    - 파라미터의 값을 출력함
```bash
juchajam@ubuntu:~$ rosparam get <파라미터 이름>
```
- rosparam set <파라미터 이름> [파라미터 값]
    - 파라미터의 값을 지정함
```bash
juchajam@ubuntu:~$ rosparam set <파라미터 이름> [파라미터 값]
```

### teleop_twist_keyboard
- 키보드 입력을 받아 /cmd_vel 토픽의 geometry_msgs/Twist 메시지로 publish 하는  노드
- 설치
```bash
$ sudo apt install ros-melodic-teleop-twist-keyboard
```
- 실행
```bash
$ rosrun teleop_twist_keyboard teleop_twist_keyboard.py
```

### roslaunch
- roscore와 launch 파일에 있는 노드들을 실행시키는 명령
- launch 파일은 `패키지 디렉토리/launch`에 만든다.
- roslaunch 실행
```bash
$ roslaunch <패키지이름> <런치파일이름>
```
- launch 파일은 <launch></launch> 태그 사이에 내용을 입력한다.
- node 태그는 패키지 이름, 노드 타입(실행파일 이름), 노드 이름을 입력한다.
- param 태그는 파라미터 이름, 값, 타입을 입력한다.