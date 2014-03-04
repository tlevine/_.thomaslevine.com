import os

import nose.tools as n
from microblog_email.parse import parse

from microblog_email import receive_messages

fixtures = {}
for fn in ['forwarded', 'not-forwarded']:
    with open(os.path.join('microblog_email','test','fixtures', fn), 'rb') as fp:
        fixtures[fn] = (fp.read())

def forwarded(*args, **kwargs):
    for i in range(3):
        yield fixtures['forwarded']

def not_forwarded(*args, **kwargs):
    for i in range(3):
        yield fixtures['not-forwarded']

expected_forwarded = {'20140303035053.GA18216': ('20140303035053.GA18216', 1393818653.0, 'aoeuaoeu', 'oeu\r\n')}
expected_not_forwarded = {}

def test_no_target():
    observed = receive_messages('not host', 'not address', 'not password',
                                mailbox = forwarded)
    n.assert_equal(observed, expected_forwarded)

def test_target_dict():
    observed = {}
    receive_messages('not host', 'not address', 'not password',
                     target = observed,
                     mailbox = forwarded)
    n.assert_equal(observed, expected_forwarded)

def test_forwarded():
    observed = receive_messages('not host', 'not address', 'not password',
                                sending_address = 'sending@thomaslevine.com',
                                forwarding_address = 'forwarding@thomaslevine.com',
                                mailbox = forwarded)
    n.assert_equal(observed, expected_forwarded)

    observed = receive_messages('not host', 'not address', 'not password',
                                sending_address = 'sending@thomaslevine.com',
                                forwarding_address = None,
                                mailbox = forwarded)
    n.assert_equal(observed, expected_not_forwarded)

def test_sending():
    observed = receive_messages('not host', 'not address', 'not password',
                                sending_address = 'sending@thomaslevine.com',
                                forwarding_address = 'forwarding@thomaslevine.com',
                                mailbox = not_forwarded)
    n.assert_equal(observed, expected_forwarded)

    observed = receive_messages('not host', 'not address', 'not password',
                                sending_address = None,
                                forwarding_address = 'sending@thomaslevine.com',
                                mailbox = not_forwarded)
    n.assert_equal(observed, expected_not_forwarded)
