import email
from _.parse import parse

def mailbox(host:str, address:str, password:str):
    M = imaplib.IMAP4_SSL(host)
    M.login(address, password)
    M.select('INBOX')
    typ, data = M.search(None, 'ALL')
    nums = data[0].split()

    try:
        for num in nums:
            if num == '':
                continue
            num, data = M.fetch(num, '(RFC822)')
            yield parse(data[0][1])

    except GeneratorExit:
        M.close()
        M.logout()
