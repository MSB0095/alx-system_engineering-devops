#!/usr/bin/python3

"""Query Reddit API to get the number
of subscribers on a subreddit"""
from requests import get
from sys import argv

headers = {'User-Agent': 'MSB0095', 'X-Forwared-For': 'Bar'}


def number_of_subscribers(subreddit):
    """return the number of subscribers
    Query Reddit API to get the number"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    response = get(url, headers=headers, allow_redirects=False)
    data = response.json()
    try:
        if 'error' in data.keys():
            return 0
        else:
            return data['data']['subscribers']
    except Exception as e:
        return 0


if __name__ == "__main__":
    print(number_of_subscribers(argv[1]))
