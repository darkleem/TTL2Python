# TTL2Python
Teraterm macro -> Python

현재 파트 내에 사용 중인 매크로는 대부분 ttl 파일로 작성된 teraterm용 매크로 입니다.

이 스크립트는 개인 리눅스 PC나 다른 SSH 프로그램에서도 간단한 python 설치만 있으면 동작이 되도록 변경해서 실행합니다.



## [개발환경]

* Python 2.7
* 사용 library : [pexpect](https://pexpect.readthedocs.io/en/stable/install.html#requirements)
* spawn사용으로 POSIX에서만 동작

## [사용방법]
* [python 설치](https://wikidocs.net/8#_2)
* pip or easy_install 사용이 가능하다면 [Link](https://pexpect.readthedocs.io/en/stable/install.html#requirements)와 같이 설치
* 수동 설치의 경우 첨부된 Setup의 tar 파일들의 압축을 해제
* spawn → ptyprocess → pexpect 순서로 설치<br>
( 압축 해제한 폴더 내의 setup.py를 이용하여 설치, (명령 예) python setup.py install )
<br>
<br>
* 중요 : launcher_ttl.py와 ttl폴더가 같은 위치에 존재해야 합니다.
* ttl 폴더 내에 .ttl(teraterm macro) 파일 들을 넣어 사용하면 됩니다.
* python launcher_ttl.py 로 실행하면, ttl폴더에 든 목록이 출력됩니다.
* 이후 원하는 것의 번호를 입력하고 Enter를 실행하면 동작합니다.
![menu](/img/manual.jpg)

## [참고]

* Source : [Link](https://github.com/darkleem/TTL2Python)
* 수동 설치 파일 : [Link](https://github.com/darkleem/TTL2Python/tree/master/setup)
