from email import message_from_bytes
from email.utils import parsedate
from time import mktime
import datetime

def parse(message:bytes) -> tuple:
    m = message_from_bytes(message)
    if not {'subject','date'}.issuperset(m.keys()):
        return None
    date = _parse_date(m['date'])
    subject = m['subject']
    body = m.get_payload()
    return date, subject, body

def _parse_date(raw_date:str) -> datetime.datetime:
    return datetime.datetime.fromtimestamp(mktime(parsedate(raw_date)))
