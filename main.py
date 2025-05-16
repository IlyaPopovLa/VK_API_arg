import requests
import os
import argparse
from dotenv import load_dotenv
from urllib.parse import urlparse


def shorten_link(url, token):
    api_url = "https://api.vk.ru/method/utils.getShortLink"
    params = {
        'access_token': token,
        'v': '5.199',
        'url': url
    }

    response = requests.get(api_url, params=params)
    response.raise_for_status()
    shorten_link_result = response.json()

    if 'response' in shorten_link_result:
        return shorten_link_result['response']['short_url'], None
    return shorten_link_result['error']['error_msg'], None


def count_clicks(link, token):
    api_url = "https://api.vk.ru/method/utils.getLinkStats"
    params = {
        'access_token': token,
        'v': '5.199',
        'key': link,
        'interval': 'forever',
    }

    response = requests.get(api_url, params=params)
    response.raise_for_status()
    count_clicks_result = response.json()

    if 'response' in count_clicks_result and count_clicks_result['response']['stats']:
        return count_clicks_result['response']['stats'][0]['views']
    return None


def is_shorten_link(url, token):
    parsed_url = urlparse(url)
    api_url = "https://api.vk.ru/method/utils.getLinkStats"
    params = {
        'access_token': token,
        'v': '5.199',
        'key': parsed_url.path.lstrip('/')
    }

    response = requests.get(api_url, params=params)
    response.raise_for_status()
    is_shorten_link_result = response.json()
    return 'response' in is_shorten_link_result


def main():
    load_dotenv()
    parser = argparse.ArgumentParser('Выполняет скрипт с аргументом url')
    parser.add_argument('url', help='Введите ссылку')
    args = parser.parse_args()
    token = os.environ.get("VK_TOKEN")

    try:
        if is_shorten_link(args.url, token):
            link_key = urlparse(args.url).path.lstrip('/')
            clicks = count_clicks(link_key, token)
            print(f"Количество кликов: {clicks if clicks is not None else 'статистика недоступна'}")
        else:
            short_url, error = shorten_link(args.url, token)
            if error:
                print(f"Ошибка при сокращении: {error}")
            else:
                print(f"Сокращенная ссылка: {short_url}")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка сети: {e}")


if __name__ == "__main__":
    main()