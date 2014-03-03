import json
import datetime

from bottle import Bottle, request, response, abort, redirect

from microblog_web.query import page
import microblog_web.templates as templates

messages = {}
app = Bottle()

@app.get('/')
def root():
    return templates.render_root(messages)

@app.get('/<message_id>')
def post(message_id):
    if message_id in messages:
        return templates.render_post(messages[message_id])
    else:
        abort(404, "There's no post with this message-id.")

@app.route('/<message_id>/')
def slash(message_id):
    redirect('/' + message_id)
