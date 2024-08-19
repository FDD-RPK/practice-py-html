# 사용자 요청에 대해 응답하는 프로그램(http 서버, 웹 서버)을 만들자
# http서버위에서 돌아가는 프로그램을 만들자
# html ---> 요청 ---> 우리프로그램 ---> 응답 ---> 사용자화면
# 위에 방식을 직접 만들려고 하면 그냥 씹 노가다 - 자동으로 해주는 프로그램 설치
# 설치 명령어 : pip install flask

import flask

# 현재 작업중인 파일을 가지고 플라스크 서버를 생성
# __name__은 플라스크 내장변수로 현재 작업 중인 파일이름
app = flask.Flask(__name__)

# 001.html을 출력할 함수를 만들고 사용자가 호출할 url을 지정한다
# annotaion - 주소를 지정
# annotation을 요청하면 그거에따른 함수를 만들어 준다
@app.route("/")
def index():
    return flask.render_template("001.html")


# debug=True -> 코드를 변경하면 서버를 재시작하도록 설정
app.run(debug=True, port=8081)