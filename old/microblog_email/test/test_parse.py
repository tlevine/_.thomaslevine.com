import os

import nose.tools as n

from microblog_email.parse import parse

def expect(forwarding):
    return ('20140303035053.GA18216', 1393818653.0, 'sending@thomaslevine.com', forwarding, 'aoeuaoeu', 'oeu\r\n')

def check_parse(fn, forwarding):
    with open(os.path.join('microblog_email','test','fixtures',fn), 'rb') as fp:
        observed = parse(fp.read())
        n.assert_tuple_equal(observed, expect(forwarding))

testcases = [
    ('forwarded', 'forwarding@thomaslevine.com receiving@thomaslevine.com'),
    ('not-forwarded', ''),
]
def test_parse():
    for fn, forwarding in testcases:
        yield check_parse, fn, forwarding
