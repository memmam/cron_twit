import tweepy
from datetime import date

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# Calculate the number of times this has been reposted
d1 = date.today()
d2 = date(2024, 10, 18)
date_diff = (d1-d2).days//7

# Body of tweet
tweet = f"""This account is no longer in active use aside from replies \
and retweets. I can now be found on Bsky, Mastodon, and Tumblr, see attached \
image.

This is an automated tweet, and will be repeated once per week. This tweet \
has been repeated {date_diff} times."""

# Get auth tokens
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api_v1 = tweepy.API(auth)
api_v2 = tweepy.Client(consumer_key=consumer_key,
                       consumer_secret=consumer_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret)

# Upload image and add alt text
media_ids = []
result = api_v1.media_upload(filename="where.png")
api_v1.create_media_metadata(result.media_id, "Insert alt text here")
media_ids.append(result.media_id)

# Send tweet
api_v2.create_tweet(text=tweet, media_ids=media_ids)
