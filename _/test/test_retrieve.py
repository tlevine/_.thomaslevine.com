import nose.tools as n

from _.retrieve import mailbox

class FAKE_IMAP4_SSL:
    def __init__(self, host):
        pass
    def login(self, address, password):
        pass
    def select(self, mailbox):
        n.assert_equal(mailbox, 'INBOX')
    def search(self, a, b):
        n.assert_is_none(a)
        n.assert_equal(b, 'ALL')
        return None, ['1 2 3 4']
    def fetch(self, num, a):
        n.assert_equal(a, '(RFC822)')
        content = {'1': 'one', '2': 'two', '3': 'three', '4': 'four'}[num]
        return None, [[None,content]]
    def close(self):
        pass
    def logout(self):
        pass

def test_mailbox():
    host = address = password = 'abcd'
    m = mailbox(host, address, password, IMAP4_SSL = FAKE_IMAP4_SSL, sleep = lambda x:None)
    n.assert_equal(next(m), 'one')
    n.assert_equal(next(m), 'two')
    n.assert_equal(next(m), 'three')
    n.assert_equal(next(m), 'four')
