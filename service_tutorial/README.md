# service_tutorial
직접 작성한 AddTwoInts 서비스로 통신하는 패키지

### Service Node
- name :
- service :
- srv : 
- 노드 설명

## srv 만드는 법
1. 패키지 안에 srv 디렉토리를 만든다.
2. .srv 확장자의 파일을 만든다.
3. 안에 내용을 작성한다.
4. CMakelists.txt에서 설정한다.
5. 빌드시 생성된다.

### srv 파일은 ---을 기준으로 나뉜다.
- 위쪽은 reuqest, 서비스 클라이언트가 요청을 보낼 때 사용한다.
- 아래쪽은 response, 서비스 서버가 응답을 보낼 때 사용한다.
