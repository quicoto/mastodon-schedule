#!/usr/bin/env python3
# encoding=utf8

import os
import argparse
import json
from mastodon import Mastodon

# parse arguments
parser = argparse.ArgumentParser (description = 'Generate an HTML archive of a mastodon user.')
parser.add_argument ('--instance', required=True, help='url to your instance')
parser.add_argument ('--access-token', required=True, help='token providing access to your account')
args = parser.parse_args()

# connect to mastodon
mstdn = Mastodon(
		access_token = args.access_token,
		api_base_url = args.instance
		)
user = mstdn.account_verify_credentials();

fileName = 'posts.json'

with open(fileName, 'r') as f:
  posts = json.load(f)['posts']

  # Only post the latest available
  if len(posts) > 0:
    # We only want to post 1 item at a time
    mstdn.status_post(
      status = posts[0],
      visibility = "public",
      language = "en"
    )

    # Remove the item we just posted from the list of posts
    posts = posts[1:]

    # Update the file with the posts
    with open(fileName, 'w') as f:
      f.write(json.dumps({'posts': posts}))

