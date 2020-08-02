import requests
import argparse
import logging
import sys
import os

from dotenv import load_dotenv

load_dotenv()


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--link")
    return parser


def get_shorten(token, link):
    url = r'https://api-ssl.bitly.com/v4/shorten'
    headers = {'Authorization': 'Bearer {}'.format(token),
               'Content-Type': 'application/json'}
    data = {'long_url': link}
    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    return response.json()['link']


def get_clicks(token, bitlink):
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    params = {'unit': 'day', 'units': '-1'}
    headers = {f'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()
    return response.json()


def main():
    parser = create_parser()
    namespace = parser.parse_args()
    logging.basicConfig(level=logging.DEBUG)
    bitly_token = os.environ['BITLY_TOKEN']
    link = namespace.link
    if link.startswith('bit.ly'):
        logging.info(get_clicks(bitly_token, link))
    else:
        logging.info(get_shorten(bitly_token, link))


if __name__ == '__main__':
    main()
