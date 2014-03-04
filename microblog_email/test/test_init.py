import os

import nose.tools as n
from microblog_email.parse import parse

from microblog_email import receive_messages

fixtures = {}
for fn in ['forwarded', 'not-forwarded']:
    with open(os.path.join('microblog_email','test','fixtures', fn), 'rb') as fp:
        fixtures[fn] = (fp.read())

def three_forwarded(*args, **kwargs):
    for i in range(3):
        yield fixtures['forwarded']

def three_not_forwarded(*args, **kwargs):
    for i in range(3):
        yield fixtures['not-forwarded']

expected_forwarding = {'20140303035053.GA18216': ('20140303035053.GA18216', 1393818653.0, 'aoeuaoeu', 'oeu\r\n')}
expected_not_forwarding = {}

def test_target_none():
    observed = receive_messages('not host', 'not address', 'not password',
                                mailbox = three_forwarded)
    n.assert_equal(observed, expected_forwarding)

def test_target_dict():
    observed = {}
    receive_messages('not host', 'not address', 'not password',
                     target = observed,
                     mailbox = three_forwarded)
    n.assert_equal(observed, expected_forwarding)

def test_forwarding():
    observed = receive_messages('not host', 'not address', 'not password',
                                sending_address = 'sending@thomaslevine.com',
                                forwarding_address = 'forwarding@thomaslevine.com',
                                mailbox = forwarding)
    n.assert_equal(observed, expected_forwarding)

    observed = receive_messages('not host', 'not address', 'not password',
                                sending_address = 'sending@thomaslevine.com',
                                forwarding_address = None,
                                mailbox = forwarding)
    n.assert_equal(observed, expected_not_forwarding)

def test_sending():
    observed = receive_messages('not host', 'not address', 'not password',
                                sending_address = 'sending@thomaslevine.com',
                                forwarding_address = 'forwarding@thomaslevine.com',
                                mailbox = not_forwarding)
    n.assert_equal(observed, expected_forwarding)

    observed = receive_messages('not host', 'not address', 'not password',
                                sending_address = None,
                                forwarding_address = 'sending@thomaslevine.com',
                                mailbox = not_forwarding)
    n.assert_equal(observed, expected_not_forwarding)
