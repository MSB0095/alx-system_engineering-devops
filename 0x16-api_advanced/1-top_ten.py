#!/usr/bin/python3
"""
Query Reddit API to get the titles of the first 10 hot posts
for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts for a given subreddit.
    If not a valid subreddit, print None.
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-Agent': 'MSB0095'}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
