import nose.tools as n

import microblog_web.query as query

seq_testcases = [
    (range(100), 0, 14, reversed(range(86,100))),
    ('honunhnozzezztzzzuzzzozzzeuthaaa', 0, 3, 'zzz'),
]

def check_seq(messages, start, end, expected):
    observed = query.seq(messages, start, end)
    n.assert_list_equal(list(observed), list(expected))

def test_seq():
    for messages, start, end, expectation in seq_testcases:
        yield check_seq, messages, start, end, expectation
