import json
import datetime

from bottle import Bottle, request, response, abort, redirect

import microblog_web.query as query
import microblog_web.templates as templates

messages = {}
app = Bottle()

@app.get('/')
def root():
    return templates.render_root(query.seq(messages, 0, 10))

@app.get('/<identifier>')
def post(identifier):
    if identifier in messages:
        return templates.render_post(messages[identifier])
    else:
        abort(404, "There's no post with this identifier.")

@app.route('/<identifier>/')
def slash(identifier):
    redirect('/' + identifier)
