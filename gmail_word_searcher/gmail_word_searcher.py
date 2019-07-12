import os
import sys
import base64
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


def content_creator(headers):
    """
    Returns the fields 'Date', 'From' and 'Subject'
    in the email with the 'word' finded.
    """
    content = {}
    for header in headers:
        if header['name'] == 'Date':
            content['Date'] = header['value']
        elif header['name'] == 'From':
            content['From'] = header['value']
        elif header['name'] == 'Subject':
            content['Subject'] = header['value']
    return content


def decoder(encoded):
    """
    Returns the email body decoded.
    """
    try:
        decoded = base64.urlsafe_b64decode(encoded).decode('utf-8')
        return str(decoded)
    except (AttributeError, UnicodeDecodeError) as e:
        print("ERROR - Object can't be decoded: {}".format(e))


def body(payload):
    """
    Checks the format of the 'payload' of the email
    (some types of email have different types of 'body').
    Then, returns the 'body' decoded (Gmail mails body comes
    encoded by urlsafe_base64).
    """
    try:
        if 'parts' in payload:
            if payload['parts'][0]['mimeType'] == 'multipart/alternative':
                raw = payload['parts'][0]['parts'][0]['body']['data']
            else:
                raw = payload['parts'][0]['body']['data']
        else:
            raw = payload['body']['data']
    except KeyError:
        return ''
    body = decoder(raw)
    return body


def subject(headers):
    """
    Searches for the key 'Subject' in email headers
    then returns the value of this key (the email
    subject title).
    """
    for header in headers:
        if header['name'] == 'Subject':
            return header['value']


def analyzer(email, word):
    """
    Gets the 'payload' and 'headers' from email,
    and check if the value of 'word' is in the
    email subject OR body. If it is, then the
    'content constructed' is returned.
    """
    payload = email['payload']
    headers = payload['headers']
    if word in subject(headers) or word in body(payload):
        return content_creator(headers)


def get_email(msg, service):
    """
    Returns one individual email (full data)
    by it's message id.
    """
    msg_id = msg['id']
    email = service.users().messages().get(userId='me',
                                           id=msg_id).execute()
    return email


def get_message_ids(service):
    """
    Returns all the message ids from the user
    'INBOX'.
    """
    msg_list = service.users().messages().list(userId='me',
                                               labelIds='INBOX').execute()
    message_ids = msg_list['messages']
    return message_ids


def login():
    """
    Log in trough the 'readonly' Gmail API scope
    and returns the authorized connection.
    A web browser comes up to make the first login, but
    after that, the token.json file will do the job.
    """
    try:
        scope = 'https://www.googleapis.com/auth/gmail.readonly'
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', scope)
            creds = tools.run_flow(flow, store)
        service = build('gmail', 'v1', http=creds.authorize(Http()))
    except Exception as e:
        print(e)
        sys.exit()
    return service


def run(word):
    """
    Calls the function to authenticate on Gmail
    and iterates over the user emails. If the email
    haves the 'word' in it's subject or body, then the
    'date', 'from' and 'subject' are shown.
    Returns the count of items found.
    """
    service = login()
    message_ids = get_message_ids(service)
    count = 0
    for msg in message_ids:
        email = get_email(msg, service)
        content = analyzer(email, word)
        if content:
            print("INFO - The word '{}' was found in: ".format(word))
            print("Date: {}, From: {}, Subject: {}".format(content['Date'],
                                                           content['From'],
                                                           content['Subject']))
            count += 1
    total = "INFO - Finished. Total of email(s) found: {}".format(count)
    return total


def user_entry():
    """
    $WORD: word to be searched. Argparser
    was not used because the gmail library
    has it's own argparser instance.
    """
    if 'WORD' not in os.environ:
        print("ERROR - The environment variable 'WORD' was not exported")
        sys.exit()
    return os.environ.get('WORD')


def main():
    word = user_entry()
    print(run(word))
    return 0


if __name__ == '__main__':
    sys.exit(main())
