import flask

app = flask.Flask(__name__)

@app.route('/')
def aaa():
    return flask.render_template('002.html')

@app.route('/insa')
def bbb():
    return flask.render_template('insa.html')

app.run(debug=True, port=8081)

