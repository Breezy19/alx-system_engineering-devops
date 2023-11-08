#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit.
If no results are found or if it's an invalid subreddit, it returns None.
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API for hot articles of a subreddit.

    :param subreddit: Name of the subreddit
    :param hot_list: Accumulator for hot article titles
    :param after: ID of the last article in the previous request
    :return: List of hot article titles or None if invalid subreddit
    """
    if hot_list is None:
        hot_list = []

    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'akram'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    # Check if the subreddit is not valid or the request was redirected
    if response.status_code != 200 or response.history:
        return None

    try:
        data = response.json()
    except ValueError:
        return None

    # Check if there are articles in the subreddit
    posts = data.get('data', {}).get('children', None)
    if not posts:
        return None

    hot_list.extend(child['data']['title'] for child in posts)

    after = data['data'].get('after', None)
    if after is None:  # No more pages, return the list
        return hot_list

    # Recursively call with the next page's 'after' ID
    return recurse(subreddit, hot_list, after)


if __name__ == '__main__':
    # This section is typically used to parse command line arguments
    # and is left as a placeholder for further implementation.
    pass
