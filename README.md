# Gmail Word Searcher
[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat)](/LICENSE) [![Python](https://img.shields.io/badge/python-3.6-blue.svg)]()

A **secure** *pythonic* gmail word searcher. It's searches for a specific word on your Gmail account inbox and shows which email contains this word.

# Getting Started

### Prerequisites

To get started, the user needs to allow the authentication by **Gmail API**, following these steps:

* Go to [Gmail API link](https://console.developers.google.com/).
* Go to the lisf of projects and click on 'New Project'.
* Give your project a name of your preference and create the project.
* Select your project and go to `Credentials -> OAuth consent screen`. Use the name **gmail-word-searcher.py** in the *app name* and Save.
* Go to `Credentials -> Create Credentials -> OAuth client ID -> Application type 'Other' -> Name it 'Gmail Word Searcher' -> Press 'OK' in 'Oauth Client Popup'`
* Click on *Download* icon to get your *client_secret.json* .

## Installing

To install **Gmail word Searcher** you will need to:
```
git clone https://github.com/alefeans/gmail-word-searcher.git && cd gmail-word-searcher/
pip install -r requirements.txt
```

## Usage

Move the *client_secret.json* to the **gmail-word-searcher/** directory, **rename** it to **credentials.json** and you're good to go.

The first time you use the script, a web browser will open to authenticate on Gmail. This will create a **token.json** file and you'll don't need to do this on the next execution.

```
cd gmail_word_searcher/
python gmail_word_searcher.py -w python
```

## Output

An example of the output (with the **token.json** file already filled):

```
INFO - The word 'python' was found in:
Date: Wed, 10 Jul 2019 11:00:00 +0000 (UTC), From: Medium Daily Digest <noreply@medium.com>, Subject: “Validating Python Data with Cerberus” published in Towards Data Science by Ross Rhodes
INFO - The word 'python' was found in:
Date: Tue, 09 Jul 2019 11:00:00 +0000 (UTC), From: Medium Daily Digest <noreply@medium.com>, Subject: “How to set-up a powerful API with Nodejs, GraphQL, MongoDB, Hapi, and Swagger” published in Level Up Your Code by Indrek Lasn
INFO - The word 'python' was found in:
Date: Mon, 08 Jul 2019 16:30:00 +0000 (UTC), From: "HackerNoon.com" <letters@medium.com>, Subject: Today I Shut Down Our Servers (and more top tech stories)
INFO - The word 'python' was found in:
Date: Mon, 08 Jul 2019 11:35:38 +0000 (UTC), From: Medium Daily Digest <noreply@medium.com>, Subject: “The Secret to Being a Top Developer Is Building Things! Here’s a List of Fun Apps to Build!” published in Better Programming by Indrek Lasn
INFO - The word 'python' was found in:
Date: Sun, 07 Jul 2019 11:16:52 +0000 (UTC), From: Medium Daily Digest <noreply@medium.com>, Subject: “How To Set Up Django with Postgres, Nginx, and Gunicorn on Ubuntu 14.04” published by Nitin Raturi
INFO - The word 'python' was found in:
Date: Fri, 05 Jul 2019 23:06:27 +0000, From: Quora <curiosity-noreply@quora.com>, Subject: Still curious about "How does Instagram use Django?"
INFO - The word 'python' was found in:
Date: Wed, 03 Jul 2019 11:00:00 +0000 (UTC), From: Medium Daily Digest <noreply@medium.com>, Subject: “Further Dangers of Large Heaps in Go” published in Ravelin Tech by Phil Pearl
INFO - The word 'python' was found in:
Date: Tue, 02 Jul 2019 11:34:00 +0000 (UTC), From: Medium Daily Digest <noreply@medium.com>, Subject: “How the CIA made Google” published in INSURGE intelligence by Nafeez Ahmed
INFO - Finished. Total of email(s) found: 8
```


## To Do

* Include unit tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
