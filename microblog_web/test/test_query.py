import nose.tools as n

import microblog_web.query as query

seq_testcases = [
    (query.seq, 'agz', dict(zip(range(10), 'aaaaagazga')), 0, 3),
    (query.seq, 'acb', dict(zip([3,1,2,-23,0], 'abcaz')), 0, 3),
]

def check(func, expected, *args):
    observed = func(*args)
    n.assert_list_equal(list(observed), list(expected))

def test():
    for args in seq_testcases:
        yield tuple([check] + list(args))
