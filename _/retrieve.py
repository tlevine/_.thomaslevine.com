import imaplib

def mailbox(host:str, address:str, password:str):
    try:
        M = imaplib.IMAP4_SSL(host)
        M.login(address, password)
        M.select('Inbox')
        typ, data = M.search(None, 'ALL')
        nums = data[0].split()
        for num in nums:
            if num == '':
                continue
            num, data = M.fetch(num, '(RFC822)')
            yield data[0][1]

    except GeneratorExit:
        M.close()
        M.logout()
