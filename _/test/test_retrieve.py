class FAKE_IMAP4_SSL:
    def search(*args):
        return ['1 2 3 4']
    def fetch(num):
        return {'1': 'one', '2': 'two', '3': 'three', '4': 'four'}

def test_mailbox():
    host = address = password = 'abcd'
    m = mailbox(host, address, password, IMAP4_SSL = FAKE_IMAP4_SSL, sleep = lambda x:None)
    n.assert_equal(next(m), 'one')
    n.assert_equal(next(m), 'two')
    n.assert_equal(next(m), 'three')
    n.assert_equal(next(m), 'four')
