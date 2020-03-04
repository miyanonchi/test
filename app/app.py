from bottle import route, run

@route('/')
def hello():
    return "<h1>Hello Spinnaker!</h1>"

run(host='0.0.0.0', port=8080, debug=True)
