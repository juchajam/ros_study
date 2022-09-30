## 과제2
- yh_star 패키지를 만들고 publisher 노드 1개, subscriber 노드 1개를 만든다.
- publisher 노드의 이름은 yh_star_pub이고, yh_star_topic이라는 이름의 토픽으로 0.5초에 한번 메시지를 publish한다.
- subscriber 노드의 이름은 yh_star_sub이고, ys_star_pub이 publish하는 메시지를 subscribe한다.
- yh_star_pub은 현재 시간과 처음 값은 1이고 매번 1씩 증가하는 정수를 YhStarMsg 메시지에 담아 publish한다.
- yh_star_sub은 subscribe한 메시지 안의 정수에 따라 printf()함수로 별을 출력한다.(python이면 print())
### ex)
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