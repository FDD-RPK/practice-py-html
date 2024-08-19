import flask

app = flask.Flask(__name__)

# SSR(Server Side Rendering) : 서버가 HTML로 응답한다
# CSR(Client Side Rendering) : 서버가 json으로 응답 + 클라이언트가 뷰(화면)를 생성
@app.route("/exam01", methods=['GET'])
def index():
    # render_template은 SSR방식으로 응답 생성 - HTML파일의 이름 필요
    return flask.render_template('exam01.html')

@app.route("/exam02", methods=['GET'])
def index2():
    return flask.render_template('exam02.html')

@app.route("/exam03")
def exam03():
    # js의 location.search에 해당
    # js에서 2개 이상의 값을 가져왔으면 type은 dictionary
    # dictionary에서 값 꺼내기 : flask.request.args['pageno']
    #   만약 키가 없다면 -> KeyError
    # 딕셔너리에서 값 꺼내기 2 : flask. request.args.get('pageno')
    #   키가 없는 경우 -> None
    pageno = flask.request.args.get('pageno')

    # 파이썬의 뷰는 확장자는 html이지만 html이 아니라 jinja2라고 하는 기술
    # jinja2에 pageno라는 값을 넘기면 {{pageno}}형식으로 출력할 수 있다
    return flask.render_template('exam03.html', pageno=pageno)


# debug=True -> 파이썬 소스 내용이 변경되면 재실행해라
app.run(debug=True, port=8081)