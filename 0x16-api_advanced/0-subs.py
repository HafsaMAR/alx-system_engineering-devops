#!/usr/bin/python3
"""Function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0."""

import requests


def number_of_subscribers(subreddit):
    """Construct the URL for the subreddit's about page in JSON format"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()

        data = response.json().get("data")
        return data.get("subscribers")
    except requests.HTTPError as e:
        if e.response.status_code == 404:
            return 0
        else:
            return None
    except requests.RequestException as e:
        return None
    # if response.status_code == 404:
    #     return 0

    # else:
    #     data = response.json().get("data")

    #     return data.get("subscribers")

    # response = requests.get(url, headers={'User-Agent': 'app/1.0'})
    # if response.status_code == 200:
    #     js_data = response.json()
    #     subscribers = js_data['data']['subscribers']
    #     return subscribers
    # else:
    #     return 0
