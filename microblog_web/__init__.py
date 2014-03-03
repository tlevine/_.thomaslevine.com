import json
from bottle import Bottle, request, response, abort, redirect, view

from microblog_web.query import page

messages = {}
app = Bottle()

@app.get('/')
def root():
    response.set_header('Content-Language', 'en')
    response.set_header('Content-Type', 'application/json; charset=utf-8')
    response.status = 200
    return json.dumps(messages)
    return json.dumps(page(messages, 0))

@app.get('/<message_id>')
@view('post')
def post(message_id):
    if message_id in messages:
        datestamp, subject, body = messages[message_id]
        return {'datestamp':datestamp,'subject':subject,'body':body}
    else:
        abort(404, "There's no post with this message-id.")

@app.route('/<message_id>/')
def slash(message_id):
    redirect('/' + message_id)
