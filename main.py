import requests
import os
import argparse
from dotenv import load_dotenv
load_dotenv()


def get_parser_args():
    parser = argparse.ArgumentParser(description='Bitly url shorterer')
    parser.add_argument(
        'link',
        help='Enter link you want to be shorten(e.g. https://google.com)'
             ' or bitlink(e.g. bit.ly/xxxxx) to get number of clicks'
    )
    return parser.parse_args()


def create_bitlink(long_url, token):
    url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {'Authorization': 'Bearer {}'.format(token)}
    payload = {'long_url': long_url}

    short_url_info = requests.post(
        url,
        json=payload,
        headers=headers
    )    
    return short_url_info.json()['link']


def is_bitlink(link, token):
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{}'.format(link)
    headers = {'Authorization': 'Bearer {}'.format(token)}
    
    return requests.get(url, headers=headers).ok


def get_click_summary(link, token):
    url = 'https://api-ssl.bitly.com/v4/bitlinks/{}/clicks/summary'.format(link)
    headers = {'Authorization': 'Bearer {}'.format(token)}

    return requests.get(url, headers=headers).json()['total_clicks']


if __name__ == '__main__':
    args = get_parser_args()
    token = os.getenv('TOKEN')
    link = args.link
    if is_bitlink(link, token):
        print('Total clicks: {}'.format(get_click_summary(link, token)))
    else:
        try:
            if requests.get(link).ok:
                print('Bitlink: {}'.format(create_bitlink(link, token)))
            else:
                print("Link doesn't exist")
        except requests.exceptions.RequestException:
            print('Invalid url')
