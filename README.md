# test-api

test용 API

## Tech

- FastAPI : 파이썬 3.6+ 으로 API서버를 구축하기 위한 모던하고, 빠른 웹 프레임 워크

## Installation

### 방법 1 - local

#### fastapi 설치

```sh
$ pip3 install fastapi
```

#### uvicorn 설치

```sh
$ pip3 install uvicorn
```

#### fastapi + uvicorn 실행

```sh
$ uvicorn main:app --reload --host=0.0.0.0 --port=8000
```

- 위 방법이 안될 경우, 아래 방법으로 실행

```sh
$ python3 -m uvicorn main:app --reload --host=0.0.0.0 --port=8000
```

### 방법 2 - docker

#### docker build 하기

```sh
$ docker build -t fastapi .
```

#### 컨테이너 띄우기

```sh
$ docker up --build -d
```
