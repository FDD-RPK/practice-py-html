import flask

app = flask.Flask(__name__)

@app.route("/exam07")
def exam07():
    val1 = int(flask.request.args.get('val1'))
    val2 = int(flask.request.args.get('val2'))
    result = val1 + val2
    return flask.render_template('exam07.html', result = result)

app.run(debug=True, port=8081)
