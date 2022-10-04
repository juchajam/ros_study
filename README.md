# ros_study
my first ros study

### 2022년 9월 27일 시작
- [topic_tutorial](./topic_tutorial)
    - topic_tutorial 패키지 생성
    - my_publisher, my_subscriber 노드 생성
    - 빌드
    - 실행

### 2022년 9월 28일
- [topic_tutorial](./topic_tutorial)
    - topic_tutorial 패키지에 python scripts 추가
    - py_publisher.py, py_subscriber.py 노드 생성
    - 빌드
    - 실행

- [topic_second](./topic_second)
    - topic_second 패키지 생성
    - second_pub, second_sub, py_second_pub.py, py_second_sub.py 노드 생성
    - 빌드
    - 실행

- [과제 1](./topic_test)

### 2022년 9월 29일
- [msg_tutorial](./msg_tutorial)
    - msg_tutorial 패키지 생성
    - msg 디렉토리에 Mymsg.msg 생성
    - msg_publisher, msg_subscsriber, py_msg_pub.py, py_msg_sub.py 노드 생성
    - 빌드
    - 실행

- [service_tutorial](./service_tutorial)
    - service_tutorial 패키지 생성
    - srv 디렉토리에 AddTwoInts.srv 생성
    - my_server, my_client, py_server.py, py_client.py 노드 생성
    - 빌드
    - 실행

### 2022년 9월 30일
- [과제 2 yh_star](./yh_star)
- for문 활용해서 별 찍기
    - yh_star 패키지 생성
    - yh_star_pub, yh_star_sub, yh_star_pub.py, yh_star_sub.py 노드 생성
    - 빌드
    - 실행

- [과제 3 yh_service](./yh_service)
    - yh_service 패키지 생성
    - yh_server, yh_client, yh_server.py, yh_client.py 노드 생성
    - 빌드
    - 실행

### 2022년 10월 4일
- [param_tutorial](./param_tutorial)

- [과제4](./과제4.pdf)

- [과제5](./과제5.pdf)

- [과제6](./과제6.pdf)

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