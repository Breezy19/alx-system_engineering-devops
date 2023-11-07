#!/usr/bin/python3

"""
count_words: Recursive function to count keywords in Reddit's hot articles.
"""

import requests

def count_words(subreddit, word_list, after=None, word_counts={}):
    """
    Recursively count keywords in the titles of hot articles in a subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): List of keywords to count.
        after (str, optional): The after parameter for Reddit API. Default is None.
        word_counts (dict, optional): Dictionary to store word counts. Default is an empty dictionary.

    Returns:
        None

    Example:
        count_words('programming', ['python', 'java', 'javascript'])
    """
    if not word_list:
        return

    if after is None:
        response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json', headers={'User-Agent': 'CountWordsBot'})
    else:
        response = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json?after={after}', headers={'User-Agent': 'CountWordsBot'})

    if response.status_code != 200:
        print(f"Error: Unable to fetch data from the subreddit '{subreddit}'.")
        return

    data = response.json()
    after = data['data']['after']

    for post in data['data']['children']:
        title = post['data']['title'].lower()
        for word in word_list:
            if word in title:
                if word not in word_counts:
                    word_counts[word] = 1
                else:
                    word_counts[word] += 1

    if after is not None:
        count_words(subreddit, word_list, after, word_counts)
    else:
        if not word_counts:
            print("No posts matched the keywords.")
        else:
            # Sort the results by count and then alphabetically
            sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_word_counts:
                print(f"{word}: {count}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        word_list = sys.argv[2].lower().split()
        count_words(subreddit, word_list)
