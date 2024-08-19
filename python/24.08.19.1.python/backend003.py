import flask

app = flask.Flask(__name__)

@app.route('/')
def aaa():
    return flask.render_template('introduce.html')

@app.route('/name')
def bbb() :
    return flask.render_template('name.html')

@app.route('/hoby')
def ccc() :
    return flask.render_template('hoby.html')

app.run(debug=True, port=8081)


# library 기능의 집합
# framework library+사용법
