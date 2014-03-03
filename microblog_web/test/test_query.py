import nose.tools as n

import microblog_web.query as query

seq_testcases = [
    (query.seq, 'zzg', dict(zip(range(10), 'aaaaaaagzg')), 0, 3),
]

def check(func, expected, *args):
    observed = func(*args)
    n.assert_list_equal(list(observed), list(expected))

def test():
    for args in seq_testcases:
        yield tuple([check] + list(args))
