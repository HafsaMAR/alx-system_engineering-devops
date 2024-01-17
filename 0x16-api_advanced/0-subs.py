#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0."""

import requests


def number_of_subscribers(subreddit):
    """Construct the URL for the subreddit's about page in JSON format"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "app/1.0"}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            subscribers = data["data"]["subscribers"]
            return subscribers
        else:
            return 0
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return 0
    # response = requests.get(url, headers={'User-Agent': 'app/1.0'})
    # if response.status_code == 200:
    #     js_data = response.json()
    #     subscribers = js_data['data']['subscribers']
    #     return subscribers
    # else:
    #     return 0
