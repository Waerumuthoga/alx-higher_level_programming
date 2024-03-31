#!/usr/bin/python3
""" Lists ten commits from the most recent to the oldest 
    repository "rails" by the user "rails"
    Usage:
            ./100-github_commits.py <repo name> <owner>
"""
import requests
import sys


if __name__ == "__main__":
    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1])
    header = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=header)
    try:
        json = r.json()
        for i in range(10):
            print("{}: {}".format(
                json[i].get('sha'),
                json[i].get('commit').get('author').get('name')))
    except ValueError:
        print("Not a valid JSON")
