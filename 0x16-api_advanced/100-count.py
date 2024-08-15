#!/usr/bin/python3
"""
Query Reddit API to count the occurrences of keywords in the titles of all hot posts
for a given subreddit recursively
"""
import requests


def count_words(subreddit, word_list, hot_list=[], after=None, word_count={}):
    """
    Print a sorted count of given keywords (case-insensitive) in the titles of all hot articles.
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'MSB0095'}
    params = {'after': after, 'limit': 100}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            title = post['data']['title'].lower().split()
            for word in word_list:
                word_lower = word.lower()
                word_count[word_lower] = word_count.get(word_lower, 0) + title.count(word_lower)
        after = data['data']['after']
        if after is not None:
            return count_words(subreddit, word_list, hot_list, after, word_count)
        else:
            sorted_word_count = sorted(word_count.items(), key=lambda kv: (-kv[1], kv[0]))
            for word, count in sorted_word_count:
                if count > 0:
                    print(f"{word}: {count}")
    else:
        return


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
