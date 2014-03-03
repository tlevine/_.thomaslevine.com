from microblog_email.retrieve import mailbox
from microblog_email.parse import parse

def receive_messages(args, target:dict):
    for email in mailbox(*args):
        message_id, date, subject, body = parse(email)
        target[message_id] = date, subject, body
