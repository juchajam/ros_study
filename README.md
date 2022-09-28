# ros_study
my first ros study

### 2022년 9월 27일 시작
- topic_tutorial 패키지 생성
- my_publisher, my_subscriber 노드 생성
- 빌드
- 실행

### 2022년 9월 28일
- topic_tutorial 패키지에 python scripts 추가
- py_publisher.py, py_subscriber.py 노드 생성
- 빌드
- 실행

## ROS 명령어
### roscore
- ROS Master를 실행한다.
- 노드를 켜기 전에 가장 먼저 실행
```bash
    roscore
```

### rosrun
- 노드를 실행한다.
- rosrun 패키지이름 노드이름
```bash
    rosrun <패키지이름> <노드이름>
```

### catkin_create_pkg
- 현재 위치한 작업 공간에 패키지를 생성한다.
- catkin_create_pkg 패키지이름 의존성
```bash
    catkin_create_pkg <패키지이름> <의존성1> <의존성2> .... 
```
```bash
    catkin_create_pkg topic_tutorial roscpp rospy std_msgs
```

## 과제 1
- topic_test 패키지를 만들고, cpp, python 중 원하는 언어를 선택하여 노드를 만든다.
- publisher 노드 1개, subscriber 노드 1개
- publisher 노드의 이름은 my_test_publisher이고 std_msgs 패키지의 Int64 메시지를 publish한다.
- subscriber 노드의 이름은 my_test_subscriber이고 std_msgs 패키지의 Int64 메시지를 subscribe한다.
- publisher 노드는 메시지에 0부터 100까지 숫자를 담아서 0.25초 주기로 publish한다.
- subscriber 노드는 메시지에 담긴 숫자를 출력한다.
- 메시지에 담는 숫자는 매번 1씩 증가시키고 100에 도달하면 다시 0부터 보낸다.