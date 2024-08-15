#!/usr/bin/python3
"""Query Reddit API to get the number
of subscribers on a subreddit"""
from requests import get


def number_of_subscribers(subreddit):
    """return the number of subscribers"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'MSB0095'}

    response = get(url, headers=headers)
    data = response.json()

    if response.status_code == 200:
        return data['data']['subscribers']
    else:
        return 0
