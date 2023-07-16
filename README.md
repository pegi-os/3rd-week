# 3rd week homework explanation

- 1번쨰 서비스: 첫 번째 서비스는 flask를 이용하여 웹 서비스를 구축하는 것이다. 이 웹은 localhost 5000번으로 pin을 할 예정이고, 들어가게 되면 hello world 밖에 입력이 되지 않는다. 여기서 만약에 유저가 POST로 이 웹에 10 미만의 숫자를 주게 되면 Success라는 문구를 출력받고, 10 이상의 숫자를 POST로 받게 되면 Fail이라는 문구를 출력받는 서비스이다.
- 2번쨰 서비스: 두 번째 서비스는 자연스럽게 첫 번째 서비스를 토대로 만들어진 웹 서비스에 POST 방식으로 숫자를 날리는 서비스이다. 이 서비스에서는 유저가 number의 값을 임의로 바꿀 수 있고, 1번째 서비스에서 언급했던 결과값을 받을 수 있다.

- 구축한 방법: 일단 이 서비스를 구축하기 위해서 어떤 기술이 필요할까 고민한 결과 docker build, docker run, docker network, docker pin, post-commit(구현 실패)를 이용하고자 마음을 먹었다.
- docker build, docker run, docker network, docker pin을 한꺼번에 깔끔하게 구축할 방법이 없을까 고민하다가 docker-compose라는 기능이 있는것을 알게 되었고, docker-compose를 통해 위의 4가지 일을 한꺼 번에 처리할 수 있었다.
- pre-commit은 사용자가 fail의 결과값을 출력받는 숫자를 준다면 commit을 실패시키고, Success숫자들만 commit이 먹히게 하고 싶었는데, 구현 할 때 제대로 작동이 안되어 pre-commit 작성을 완료하지 못하였다.

- git action: git action을 사용하여 사용자가 pull을 할 때마다 second.py에 제대로 된 숫자(int) 값을 넣었는지 확인을 하고 싶었는데, second.py에서 포트 5000번에 구축된 내 웹으로 숫자를 전달하는 파이썬 코드가 있어서인지 git action으로 run second.py라는 문구를 넣으면 향상 실패하는 에러를 겪었다. 따라서 어쩔수 없이 git action으로는 stop the build if there are Python syntax errors or undefined names 의 역할을 하는 Lint with ruff 밖에 구축을 못하였다.

- 
