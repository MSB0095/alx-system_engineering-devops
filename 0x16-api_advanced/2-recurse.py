#!/usr/bin/python3
"""
Query Reddit API to get the titles of all hot posts
for a given subreddit recursively
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Return a list containing the titles of all hot articles
    for a given subreddit.
    If no results are found for the given subreddit, return None.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MSB0095'}
    params = {'after': after, 'limit': 100}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            hot_list.append(post['data']['title'])
        after = data['data']['after']
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
