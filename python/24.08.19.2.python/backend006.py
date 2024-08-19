# flask의 역할
# 1. 요청,응답 생성 및 처리
# 2. url과 함수를 binding

import flask

app = flask.Flask(__name__)

@app.route("/exam04")
def exam04():
    val1 = int(flask.request.args.get('val1'))
    val2 = int(flask.request.args.get('val2'))
    result = val1 + val2
    return flask.render_template('/exam04.html', val1=val1, val2=val2, result=result)

app.run(debug=True, port=8081)
