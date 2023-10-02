# -*- coding: utf-8 -*-

import datetime
import time

import requests


def instagram():
    """Grabs top posts related to any Instagram hashtag"""
    hashtag = str(input("Enter a hashtag : "))
    start = datetime.datetime.now()
    print("\nConnecting...\n")
    url = f'https://www.instagram.com/explore/tags/{hashtag}/?__a=1'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/41.0.2228.0 Safari/537.36'}

    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print("Failed D:")
        time.sleep(3)
        exit()

    resp = r.json()
    posts = resp["graphql"]["hashtag"]["edge_hashtag_to_top_posts"]["edges"]
    if len(posts) == 0:
        print("Sorry! Nothing found :(")
        time.sleep(3)
        exit()

    print(f"Connected! - Total Posts Found : {len(posts)}\n")

    """
Description: This Python script iterates through a list of 'posts' and extracts
the 'shortcode' from each post to generate Instagram post URLs. It also calculates
the total time taken for the operation and prompts the user to press Enter to exit.

- It iterates through the 'posts' list, extracting the 'shortcode' and constructing
  Instagram post URLs for each post.
  
- It records the start and end times to calculate the total execution time.

- It prints a completion message along with the total time taken.
"""

    for post in posts:
        source = post['node']['shortcode']
        print(f'https://www.instagram.com/p/{source}')
    end = datetime.datetime.now()
    total_time = (end - start).total_seconds()
    print(f"\nDone!")

    input(f"Total time taken : {total_time} seconds")


if __name__ == '__main__':
    instagram()
