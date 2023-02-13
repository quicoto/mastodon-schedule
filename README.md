# Mastodon post scheduler

It allows you to "schedule" (or "publish later") a list of posts to be published on Mastodon. It doesn't actually use the schedule feature.

It uses GitHub actions to run the script every 1 hour. The script will check if there is a post to be published and will publish it. It will only publish 1 post at a time.
