from imaplib import IMAP4_SSL as _IMAP4_SSL
from time import sleep as _sleep

def mailbox(host:str, address:str, password:str,
            IMAP4_SSL = _IMAP4_SSL, sleep = _sleep):

    try:
        M = imaplib.IMAP4_SSL(host)
        M.login(address, password)
        M.select('Inbox')
        finished_nums = set()
        while True:
            typ, data = M.search(None, 'ALL')
            nums = data[0].split()
            for num in nums:
                if num == '':
                    # There are no results.
                    pass
                elif num in finished_nums:
                    # The message has already been loaded.
                    pass
                else:
                    num, data = M.fetch(num, '(RFC822)')
                    yield data[0][1]
            sleep(10)

    except GeneratorExit:
        M.close()
        M.logout()
