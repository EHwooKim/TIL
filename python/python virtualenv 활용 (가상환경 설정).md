# python virtualenv 활용

> 가상환경을 사용하는 이유는 패키지를 환경별로 독립적으로 관리하기 위해서이다.
>
> 예) A 프로젝트 :  B 패키지의 버전을 3.2 를 쓰는데, C 프로젝트 : B 패키지의 버전을 2.8 을 쓰는 경우 매번 설치/삭제를 할 수 없으므로 독립된 가상환경을 만들어준다.
>
> 파이썬에서는 가상환경을 만들어주는 다양한 패키지들이 있는데 우리는 python에 내장되어있는 `venv`를 사용한다.

## 1. 가상환경 설정

```bash
$ mkdir ~/내가원하는폴더위치
```

```bash
$ python -m venv ~/특정위치/버전명(혹은 가상환경 명)
```

해당 폴더를 열어보면, 아래와 같은 파일들이 있다.

```
activate	 # git bash용 (python 3.6+)
activate.bat # cmd용
activate.psl # power shell용
```

## 2. 가상환경 실행 및 종료

```bash
$ sourse ~/특정위치/버전명(혹은 가상환경명)/activate
```

```bash
$ deactivate
```

