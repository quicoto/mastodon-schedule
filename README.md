# Mastodon post scheduler

This is just proof of concept, use with caution.

It allows you to "schedule" (or "publish later") a list of posts to be published on Mastodon. *It doesn't actually use the schedule feature*, nor it let's you chose time. You could add a date to the posts, just fork this repo to get inspired.

## How does it work?

It uses GitHub actions to run the script every 1 hour. The script will check if there is a post to be published and will publish it. It will only publish 1 post at a time.
