# 과제 1
- topic_test 패키지를 만들고, cpp, python 중 원하는 언어를 선택하여 노드를 만든다.
- publisher 노드 1개, subscriber 노드 1개
- publisher 노드의 이름은 my_test_publisher이고 std_msgs 패키지의 Int64 메시지를 publish한다.
- subscriber 노드의 이름은 my_test_subscriber이고 std_msgs 패키지의 Int64 메시지를 subscribe한다.
- publisher 노드는 메시지에 0부터 100까지 숫자를 담아서 0.25초 주기로 publish한다.
- subscriber 노드는 메시지에 담긴 숫자를 출력한다.
- 메시지에 담는 숫자는 매번 1씩 증가시키고 100에 도달하면 다시 0부터 보낸다.