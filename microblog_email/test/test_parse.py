import os

import nose.tools as n

from microblog_email.parse import parse

def test_parse():
    with open(os.path.join('_','test','fixtures','email'), 'rb') as fp:
        observed = parse(fp.read())
        expected = ('20140303035053.GA18216', 1393818653.0, 'aoeuaoeu', 'oeu\r\n')
        n.assert_tuple_equal(observed, expected)
