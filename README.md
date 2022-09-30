# ros_study
my first ros study

### 2022년 9월 27일 시작
- topic_tutorial
    - topic_tutorial 패키지 생성
    - my_publisher, my_subscriber 노드 생성
    - 빌드
    - 실행

### 2022년 9월 28일
- topic_tutorial
    - topic_tutorial 패키지에 python scripts 추가
    - py_publisher.py, py_subscriber.py 노드 생성
    - 빌드
    - 실행

- topic_second
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

## 과제2
- yh_star 패키지를 만들고 publisher 노드 1개, subscriber 노드 1개를 만든다.
- publisher 노드의 이름은 yh_star_pub이고, yh_star_topic이라는 이름의 토픽으로 0.5초에 한번 메시지를 publish한다.
- subscriber 노드의 이름은 yh_star_sub이고, ys_star_pub이 publish하는 메시지를 subscribe한다.
- yh_star_pub은 시간과 정수를 YhStarMsg 메시지에 담아 publish한다.
- yh_star_sub은 subscribe한 메시지 안의 정수에 따라 printf()함수로 별을 출력한다.(python이면 print())
ex)
```console
1 -> *
2 -> *
     *
3 -> *
     **
     *
4 -> *
     **
     **
     *
5 -> *
     **
     ***
     **
     *
```
