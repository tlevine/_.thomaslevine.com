from _.retrieve import mailbox
from _.parse import parse

def _receive_messages(args, target:dict):
    for email in mailbox(*args):
        message_id, date, subject, body = parse(email)
        target[message_id] = date, subject, body

def run(messages, app):
    '''
    Args:
        messages: A dictionary of messages to populate
        app: A bottle app
    '''
    host = os.environ['posse_host']
    username = os.environ['posse_email_address']
    password = os.environ['posse_password']
    args = host, username, password)
    t = Thread(None, target = _receive_messages,
               name = 'receive', args = (args, messages))
    bottle.run(app)
