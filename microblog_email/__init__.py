from microblog_email.retrieve import mailbox as _mailbox
from microblog_email.parse import parse

def receive_messages(host:str, address:str, password:str,
                     sending_address:str = None,
                     forwarding_address:str = None,
                     target:dict = {},
                     mailbox = _mailbox):
    '''
    Retrieve messages from an IMAP mailbox. Optionally require that messages
    be sent from a particular addresss and forwarded through a particular address.

    Logging in to the IMAP mailbox:

    :param host: IMAP host (like mail.gandi.net)
    :param address: Maillbox at that host (like secret@thomaslevine.com)
    :param password: Password for that mailbox

    Validating that the email came from you:

    :param sending_address: The email address from which emails must be sent
    :param forwarding_address: The email address through which emails must be forwarded

    Mainly for testing:

    :param mailbox: a generator that emits emails (like microblog_email.retrieve.mailbox)

    Results:

    :param target: dict into which results should be placed (optional)
                   If you specify this, the dict gets updated **in place**.

    Returns a dict
    '''
    for email in mailbox(host, address, password):
        identifier, date, sent_from, forwarding, subject, body = parse(email)
        if forwarding_address is None or forwarding_address in forwarding:
            if sending_address is None or sending_address in sent_from:
                results = identifier, date, subject, body
                target[identifier] = results
