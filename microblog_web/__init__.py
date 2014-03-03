import json
from bottle import Bottle, request, response

messages = {}
app = Bottle()

@app.get('/')
def root():
    response.set_header('Content-Language', 'en')
    response.set_header('Content-Type', 'application/json; charset=utf-8')
    response.status = 200
    return json.dumps(messages)
