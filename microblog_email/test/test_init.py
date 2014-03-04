import os

import nose.tools as n

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

expect_yes = {'20140303035053.GA18216': ('20140303035053.GA18216', 1393818653.0, 'aoeuaoeu', 'oeu\r\n')}
expect_no = {}

def test_no_target():
    observed = receive_messages('not host', 'not address', 'not password',
                                mailbox = forwarded)
    n.assert_equal(observed, expect_yes)

def test_target_dict():
    observed = {}
    receive_messages('not host', 'not address', 'not password',
                     target = observed,
                     mailbox = forwarded)
    n.assert_equal(observed, expect_yes)

def test_forwarded_set_match():
    observed = receive_messages('not host', 'not address', 'not password',
                                sending_address = 'sending@thomaslevine.com',
                                forwarding_address = 'forwarding@thomaslevine.com',
                                mailbox = forwarded)
    n.assert_equal(observed, expect_yes)

    observed = receive_messages('not host', 'not address', 'not password',
                                sending_address = 'sending@thomaslevine.com',
                                forwarding_address = 'forwarding@thomaslevine.com',
                                mailbox = not_forwarded)
    n.assert_equal(observed, expect_no)

def test_forwarded_set_nomatch():
    observed = receive_messages('not host', 'not address', 'not password',
                                sending_address = 'sending@thomaslevine.com',
                                forwarding_address = 'blah@thomaslevine.com',
                                mailbox = forwarded)
    n.assert_equal(observed, expect_no)

def test_forwarded_notset():
    observed = receive_messages('not host', 'not address', 'not password',
                                sending_address = 'sending@thomaslevine.com',
                                forwarding_address = None,
                                mailbox = forwarded)
    n.assert_equal(observed, expect_yes)

    observed = receive_messages('not host', 'not address', 'not password',
                                sending_address = 'sending@thomaslevine.com',
                                forwarding_address = None,
                                mailbox = not_forwarded)
    n.assert_equal(observed, expect_yes)

@n.nottest
def test_sending():
    observed = receive_messages('not host', 'not address', 'not password',
                                sending_address = 'sending@thomaslevine.com',
                                forwarding_address = 'forwarding@thomaslevine.com',
                                mailbox = not_forwarded)
    n.assert_equal(observed, expect_yes)

    observed = receive_messages('not host', 'not address', 'not password',
                                sending_address = None,
                                forwarding_address = 'sending@thomaslevine.com',
                                mailbox = not_forwarded)
    n.assert_equal(observed, expect_no)
