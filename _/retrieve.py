import email
from _.parse import parse

class Mailbox:
    def __init__(self, host:str, address:str, password:str):
        self.address = address

    def close(self):
        self.M.close()
        self.M.logout()

    def __iter__(self):
        self.M = imaplib.IMAP4_SSL(host)
        self.M.login(address, password)
        self.M.select('INBOX')
        self.typ, self.data = self.M.search(None, 'ALL')
        self.nums = data[0].split()
        return self

    def __next__(self) -> str:
        num = self.nums.pop()
        num, data = self.M.fetch(num, '(RFC822)')
        return parse(data[0][1])
