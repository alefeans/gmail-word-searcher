import sys
import argparse
import base64
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from mysql_manager import MySQLConnector


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
    try:
        decoded = base64.urlsafe_b64decode(encoded).decode('utf-8')
        decoded = str(decoded)
        return decoded
    except Exception as e:
        print(e)


def body(payload):
    """
    Check the format of the 'payload' of the email
    (some types of email have different types of 'body').
    Then, returns the 'body' decoded (Gmail mails body comes
    encoded by urlsafe_base64).
    """
    if 'parts' in payload:
        if payload['parts'][0]['mimeType'] == 'multipart/alternative':
            raw = payload['parts'][0]['parts'][0]['body']['data']
        else:
            raw = payload['parts'][0]['body']['data']
    else:
        raw = payload['body']['data']
    body = decoder(raw)
    return body


def subject(headers):
    """
    Search for the key 'Subject' in email headers
    then returns the value of this key (the email
    subject title).
    """
    for header in headers:
        if header['name'] == 'Subject':
            return header['value']


def analyzer(email, word):
    """
    Gets the 'payload' and 'headers' from email,
    and check if the value of 'word' is finded in the
    email subject OR body. If it's finded, then the
    'content constructed' is returned. Else, returns
    empty (None).
    """
    payload = email['payload']
    headers = payload['headers']
    if word in subject(headers):
        content = content_creator(headers)
    elif word in body(payload):
        content = content_creator(headers)
    else:
        return
    return content


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
    after that, the json files with the token/credentials
    do the job.
    """
    scope = 'https://www.googleapis.com/auth/gmail.readonly'
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', scope)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))
    return service


def run(args):
    """
    Creates the mysql connection with the user parameters
    and iterate over the user emails. If the email haves
    the 'word' in it's subject or body, then the 'insert_items'
    is called to insert the content created by 'content_creator'
    in the database.
    """
    mysql = MySQLConnector(args.user, args.password, args.address)
    service = login()
    message_ids = get_message_ids(service)
    for msg in message_ids:
        email = get_email(msg, service)
        content = analyzer(email, args.word)
        if content:
            mysql.insert_items(content)
    return


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Gmail Word Finder")
    parser._action_groups.pop()
    optional = parser.add_argument_group('optional arguments')
    required = parser.add_argument_group('required arguments')
    optional.add_argument("-w", "--word",
                          help="word to find, default is 'DevOps'",
                          metavar='<word>',
                          default='DevOps')
    optional.add_argument("-u", "--user",
                          help="mysql database user, default is root",
                          metavar='$MYSQL_USER',
                          default='root')
    optional.add_argument("-a", "--address",
                          help="mysql address, default is localhost",
                          metavar='$MYSQL_HOST',
                          default='localhost')
    required.add_argument("-p", "--password",
                          help="mysql database password'",
                          metavar='$MYSQL_PASSWD',
                          required=True)
    return parser.parse_args(argv[1:])


def main(argv):
    args = parse_args(argv)
    run(args)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
