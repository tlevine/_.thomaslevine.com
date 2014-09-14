from notmuch import Database, Query
from bottle import Bottle, request, response, abort, redirect

app = Bottle()
db = Database()

@app.route('/<identifier>/')
def slash(identifier):
    redirect('/' + identifier)

@app.get('/searches/:search')
def search(search)
    query = Query(db, query).search_threads()
    return [[t.get_thread_id(), t.get_subject()] for t in query]

@app.get('/threads/:thread_id')
def thread(thread_id):
    query = notmuch.Query(db, 'thread:%s' % thread_id)
    if not query.count_threads() == 1:
        return 'Thread not found', 404
    return [[m.get_message_id(), m.get_subject()] for m in query.search_messages()]

@app.get('/messages/:message_id'):
def message(message_id):
    query = notmuch.Query(db, 'message:%s' % message_id)
    if not query.count_messages() == 1:
        return 'Message not found', 404
    return [m.get_subject(), m.get_thread_id()]

@app.get('/recent'):
def recent():
    query = notmuch.Query(db, '')
    for i, message in enumerate(query.search_messages()):
        if i >= 5:
            break
        yield [m.get_message_id(), m.get_subject]
