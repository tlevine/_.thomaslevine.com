from _.retrieve import mailbox
from _.parse import parse

def receive_messages(args, target:dict):
    for email in mailbox(*args):
        message_id, date, subject, body = parse(email)
        target[message_id] = date, subject, body
