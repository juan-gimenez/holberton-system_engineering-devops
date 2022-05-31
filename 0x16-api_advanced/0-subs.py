#!/usr/bin/python3
"""
reddit api
"""
import requests


def number_of_subscribers(subreddit):
    """ Subs of reddit """
    if type(subreddit) is not str or subreddir is None:
        return 0
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    h = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36'
    }
    resp = requests.get(url, headers=h, allow_redirects=False)
    if resp.status_code == 404:
        return 0
    else:
        result = resp.json().get('data')
        return result.get('subscribers')
