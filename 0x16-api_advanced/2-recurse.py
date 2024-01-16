#!/usr/bin/python3
"""ecursive function that queries the Reddit API and returns
a list containing the titles of all hot articles for a given
subreddit. If no results are found for the given subreddit,
the function should return None."""

import requests


def recurse(subreddit, hot_list=[], page=1, limit=100):
    if len(hot_list) >= limit:
        return hot_list

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    parameters = {"page": page}
    headers = {
        "User-Agent": "Mozilla"
    }
    response = requests.get(url, params=parameters, headers=headers)
    if response.status_code == 404:
        return None
    data = response.json()

    if "data" in data and "children" in data["data"]:
        articles = data["data"]["children"]
        for article in articles:
            hot_list.append(article["data"]["tittle"])

    if "data" in data and "after" in data["data"]:
        page += 1
        return recurse(subreddit, hot_list, page)
    return hot_list
