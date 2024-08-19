# 언어를 실행하면 모든 기능을 로딩하지는 않는다
# datetime 모듈을 가지고 와라 = import datetime
import datetime

# 서로 관련된 데이터와 함수를 모아서 클래스를 만든다
# 클래스는 객체를 만드는 설계도다
# 서로 관련된 클래스를 모아서 모듈을 만든다
print(datetime.datetime.now())

# 다른 사람이 만든 라이브러리를 가져다 사용가능
# ★import★ requests - 밑에꺼 설치 안하면 오류남
# 외부 라이브러리는 pip install로 설치 -> pip install requests - 그냥 콘솔에 적으면 됨
# 라이브러리를 이용하는 것을 이용한다고 하지 않고 의존한다고 한다
# pip로 requests에 대한 의존성을 관리했다....


import requests
response = requests.get("https://api.bithumb.com/public/ticker/")
print(response.json())

# 의존성 관리도구 - 작업중인 폴더의 위치가 바뀌어도 작업할 수 있도록 이용
# js - npm
# python - pi
# 자바 - maven, gradle