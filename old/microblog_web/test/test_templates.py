import datetime

import nose.tools as n

import microblog_web.templates as templates

def test_render_post():
    d = datetime.datetime(2014, 3, 3, 5, 27, 50, 737546)
    message = ('foobar', d.timestamp(), 'Subject goes here.', 'Body goes here.')
    result = templates.render_post(message)

    #n.assert_in(, result)
    n.assert_in('Monday, March 03 at 05:27 UTC', result)
    n.assert_in('Subject goes here.', result)
    n.assert_in('Body goes here.', result)

def test_render_root():
    d = datetime.datetime(2014, 3, 3, 5, 27, 50, 737546)
    message = ('foobar', d.timestamp(), 'Subject goes here.', 'Body goes here.')
    result = templates.render_root([message])

    n.assert_in('href="/foobar"', result)
    #n.assert_in(, result)
    n.assert_in('Monday, March 03 at 05:27 UTC', result)
    n.assert_in('Subject goes here.', result)
    n.assert_in('Body goes here.', result)
