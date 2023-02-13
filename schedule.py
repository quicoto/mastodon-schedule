#!/usr/bin/env python3
# encoding=utf8

import os
import json

fileName = 'posts.json'

with open(fileName, 'r') as f:
  posts = json.load(f)['posts']

  # Only post the latest available
  if len(posts) > 0:
    # We only want to post 1 item at a time
    status = "@ricard " + posts[0]
    print(status)

  # Remove the item we just posted from the list of posts
  posts = posts[1:]

  # Update the file with the posts
  with open(fileName, 'w') as f:
    f.write(json.dumps({'posts': posts}))

