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


def test_target_none():
    r = receive_messages('not host', 'not address', 'not password',
                         mailbox = three_forwarded)
    observed = list(r)
    n.assert_equal(len(observed), 3)

def test_target_dict():
    observed = {}
    receive_messages('not host', 'not address', 'not password',
                     target = observed,
                     mailbox = three_forwarded)
    expected = {'20140303035053.GA18216': [1393818653.0, 'aoeuaoeu', 'oeu\r\n']}
    n.assert_dict_equal(observed, expected)

'''
def test_target_none():
    receive_messages('not host', 'not address', 'not password',
                     sending_address:str = None,
                     forwarding_address:str = None,
                     target:dict = None,
                     mailbox = fake_mailbox)
'''
