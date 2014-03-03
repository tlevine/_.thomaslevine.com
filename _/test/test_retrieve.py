import nose.tools as n

from _.retrieve import mailbox

i = {
    'ran_login ': False,
    'ran_select': False,
    'ran_search': False,
    'ran_fetch ': False,
    'ran_close ': False,
    'ran_logout': False,
}

class FAKE_IMAP4_SSL:
    def __init__(self, host):
        pass
    def login(self, address, password):
        i['ran_login'] = True
    def select(self, mailbox):
        i['ran_select'] = True
        n.assert_equal(mailbox, 'INBOX')
    def search(self, a, b):
        i['ran_search'] = True
        n.assert_is_none(a)
        n.assert_equal(b, 'ALL')
        return None, ['1 2 3 4']
    def fetch(self, num, a):
        i['ran_fetch'] = True
        n.assert_equal(a, '(RFC822)')
        content = {'1': 'one', '2': 'two', '3': 'three', '4': 'four'}[num]
        return None, [[None,content]]
    def close(self):
        i['ran_close'] = True
    def logout(self):
        i['ran_logout'] = True

def test_mailbox():
    host = address = password = 'abcd'
    m = mailbox(host, address, password, IMAP4_SSL = FAKE_IMAP4_SSL, sleep = lambda x:None)

  # n.assert_true(i['ran_login'])
  # n.assert_true(i['ran_select'])
  # n.assert_true(i['ran_search'])
  # n.assert_true(i['ran_fetch'])
  # n.assert_true(i['ran_close'])
  # n.assert_true(i['ran_logout'])

    n.assert_equal(next(m), 'one')
    n.assert_equal(next(m), 'two')
    n.assert_equal(next(m), 'three')

  # n.assert_false(i['ran_close'])
  # n.assert_false(i['ran_logout'])
    n.assert_equal(next(m), 'four')
  # n.assert_true(i['ran_close'])
  # n.assert_true(i['ran_logout'])
