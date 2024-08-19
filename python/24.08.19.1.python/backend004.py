# python은 내부, 외부 많은 라이브러리에 의존한다
# python project가 설치된 모든 library를 다 사용할 수 있는 상태는 아니다
#  -> 필수 library만 사용가능 = 가볍게 하려고
# 필요한 library는 import명령으로 가져오라고 지시해야 한다
import flask

# 사용자 요청을 접수해 함수를 호출해줄 서버 프로그램이 필요하다
# 서버 프로그램은 flaks 모듈의 Flask 클래스의 객체
# 객체를 생성할 때 현재 작업중인 소스 파일이 필요하다
# 현재 작업중인 파일의 이름은 파이썬은 __name__이라는 내장 변수에 담아놓고 있다
app = flask.Flask(__name__)

# 함수는 실행하면 처리가 끝난 후 종료된다
# 백엔드에서는 사용자가 요청할 때마다 함수가 실행되기 위해 url + 함수를 엮는다(binding)

@app.route('/aaa')
def index():
    print('aaa를 실행했어요')

@app.route('/bbb')
def bbb() :
    print('bbb를 실행했어요')

app.run(debug=True, port=8081)