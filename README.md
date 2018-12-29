# Gmail Word Finder
[![MIT License](https://img.shields.io/badge/license-MIT-007EC7.svg?style=flat)](/LICENSE) [![Python](https://img.shields.io/badge/python-3.6-blue.svg)]()

A **secure** *pythonic* gmail word finder. It's searches on your Gmail account inbox for a specific word, collect it's origin, date and subject and inserts in a MySQL Database.

# Getting Started

### Prerequisites

Before running the script, the user should get the authentication by allowing the Gmail API. Follow these steps:

* Go to [Gmail API link](https://console.developers.google.com/).
* Click on the lisf of projects and select **+** to add a new one.
* Give your project a name of your preference and create the project.
* Go to `Credentials -> OAuth consent screen -> Product name shown to users`. Use the name **gmail_word_finder.py** and Save.
* Go to `Credentials -> Create Credentials -> OAuth client ID -> Application type -> Other -> Name it 'Gmail Word Finder' -> Press 'OK' in 'Oauth Client Popup' -> Click on 'Download' icon to get your client_secret.json` .
* Save the *client_secret.json* in **gmail_word_finder/** directory, rename it to *credentials.json* and you're good to go.

## Installing

Follow these steps to install **Gmail word finder**:
```
git clone https://github.com/alefeans/gmail_word_finder.git .
pip install -r requirements.txt
```

## Usage



## Tests


```
pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
