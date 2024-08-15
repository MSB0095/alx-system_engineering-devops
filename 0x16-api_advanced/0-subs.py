#!/usr/bin/python3

"""
Query Reddit API to get the number of subscribers on a subreddit
"""
from requests import get
from sys import argv

headers = {'User-Agent': 'MSB0095', 'X-Forwarded-For': 'Bar'}


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers for a given subreddit.
    Query Reddit API to get the number of subscribers.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    response = get(url, headers=headers, allow_redirects=False)
    try:
        data = response.json()
        if 'error' in data:
            return 0
        return data['data']['subscribers']
    except Exception:
        return 0


if __name__ == "__main__":
    print(number_of_subscribers(argv[1]))
