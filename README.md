# Gmail Word Finder
[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat)](/LICENSE) [![Python](https://img.shields.io/badge/python-3.6-blue.svg)]()

A **secure** *pythonic* gmail word finder. It's searches for a specific word on your Gmail account inbox, collects the fields 'origin', 'date' and 'subject' from the email and inserts in a MySQL database.

# Getting Started

### Prerequisites

To get started, the user needs to allow the authentication by **Gmail API**, following these steps:

* Go to [Gmail API link](https://console.developers.google.com/).
* Go to the lisf of projects and click on 'New Project'.
* Give your project a name of your preference and create the project.
* Select your project and go to `Credentials -> OAuth consent screen`. Use the name **gmail_word_finder.py** in the *app name* and Save.
* Go to `Credentials -> Create Credentials -> OAuth client ID -> Application type 'Other' -> Name it 'Gmail Word Finder' -> Press 'OK' in 'Oauth Client Popup'`
* Click on *Download* icon to get your *client_secret.json* .

## Installing

To install **Gmail word finder** you will need to:
```
git clone https://github.com/alefeans/gmail_word_finder.git .
pip install -r requirements.txt
```

## Usage

Move the *client_secret.json* to the **gmail_word_finder/** directory, **rename** it to *credentials.json* and you're good to go. 

The first time you use the script, a web browser will open to authenticate on Gmail. This will create a **token.json** file and you'll don't need to do this on the next execution.

```
# Export these environment variables:
# MYSQL_USER (default 'root')
# MYSQL_HOST (default 'localhost')
# WORD (word to find, default 'DevOps')
# MYSQL_PASSWD (MySQL password is required)
export MYSQL_PASSWD='test123'
cd gmail_word_finder/
python gmail_word_finder.py
```

## Output

An example of the output (with the **token.json** file already filled):

```
INFO - Database 'emails' and table 'mail_list' OK
INFO - Inserting ('Thu, 27 Dec 2018 16:51:51 +0000', '"Álefe Nascimento" <alefeans2@hotmail.com>', 'Test') on table 'mail_list'
INFO - Inserting ('Thu, 27 Dec 2018 16:23:41 +0000', '"Álefe Nascimento" <alefeans2@hotmail.com>', 'The DevOps culture') on table 'mail_list'
INFO - Inserting ('Thu, 27 Dec 2018 16:23:28 +0000', '"Álefe Nascimento" <alefeans2@hotmail.com>', 'DevOps') on table 'mail_list'
INFO - Inserting ('Tue, 11 Dec 2018 12:44:37 +0000 (UTC)', 'Medium Daily Digest <noreply@medium.com>', '“Transducers: Efficient Data Processing Pipelines in JavaScript” published in JavaScript Scene by Eric Elliott') on table 'mail_list'
```

And the data in the MySQL table:

 id_email        | date | origin  | subject |
| :---: |:---:| :---:|:---:|
| 1| Thu, 27 Dec 2018 16:51:51 +0000 | "Álefe Nascimento" <alefeans2@hotmail.com>|  The DevOps culture|


## To Do

* Include unit tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
