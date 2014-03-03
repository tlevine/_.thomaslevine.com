import re
from email import message_from_bytes
from email.utils import parsedate
from time import mktime
import datetime

def parse(message:bytes) -> tuple:
    m = message_from_bytes(message)
    message_id = _parse_message_id(m['message-id'])
    date = _parse_date(m['date'])
    subject = m['subject']
    body = m.get_payload()
    return message_id, date, subject, body

def _parse_date(raw_date:str) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(mktime(parsedate(raw_date)))

def _parse_message_id(raw_message_id):
    re.match(r'^<([^@]+).*', raw_message_id).group(1)
