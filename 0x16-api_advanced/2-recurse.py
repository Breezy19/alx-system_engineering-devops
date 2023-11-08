#!/usr/bin/python3
"""
This module contains a function that queries the Reddit API
and returns a list containing the titles of all hot articles
for a given subreddit using recursion.
"""
import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Recursively queries the Reddit API for hot articles of a subreddit.

    :param subreddit: Name of the subreddit
    :param hot_list: Accumulator for hot article titles
    :param after: Pagination parameter for next set of results
    :return: List of hot article titles or None if invalid subreddit
    """

    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'python3:alx-system_engineering-devops:v1.0.0 (by /u/username)'}
    params = {'limit': 100, 'after': after}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json()
    except ValueError:
        return None

    # Check if there are articles in the subreddit
    children = data.get('data', {}).get('children', None)
    if children is None:
        return None

    for child in children:
        hot_list.append(child['data']['title'])

    after = data['data'].get('after', None)
    if after is None:
        return hot_list

    return recurse(subreddit, hot_list, after)


if __name__ == "__main__":
    # The code for interacting with the command line can be placed here
    pass
