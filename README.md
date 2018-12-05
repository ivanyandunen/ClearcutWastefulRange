# Bitly url shorterer

This script creates short links using bitly.com service. Or shows number of clicks for existing bitlinlks.

## How to install

First you have to create account on bitly.com and generate access token in profile settings.
Then put this token to file .env in the same directory with the script.

Python 3 has to be installed. You might have to run python3 instead of python depending on system if there is a conflict with Python2. Then use pip (or pip3) to install dependencies:

```commandline
pip install -r requirements.txt
```

```commandline
usage: python main.py [-h] link

Bitly url shorterer

positional arguments:
  link        Enter link you want to be shorten(e.g. https://google.com) or
              bitlink(bit.ly/xxxxx) to get number of clicks

optional arguments:
  -h, --help  show this help message and exit

```

## Project Goals

The code is written for educational purposes on online-course for web-developers dvmn.org.