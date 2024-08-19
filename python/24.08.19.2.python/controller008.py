import flask

app = flask.Flask(__name__)

@app.route("/exam08")
def aaa():
    val1 = int(flask.request.args.get('val1'))
    val2 = int(flask.request.args.get('val2'))
    op = flask.request.args.get('op')
    result = val1 + val2
    if op == '-':
        result = val1 - val2
    else :
        result = val1 + val2
    return flask.render_template("exam08.html", val1 = val1, val2 = val2, op= op, result=result)

app.run(debug=True, port=8081)