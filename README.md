# cron_twit
A simple Python script for sending a fixed tweet. Intended for use as a Linux cronjob.

As configured, it will post the following as a tweet, as well as attach the image `where.png` with the alt text `Insert alt text here`. `{date_diff}` is replaced with the number of weeks since 2024-10-18:

```
This account is no longer in active use aside from replies and retweets. I can now be found on Bsky, Mastodon, and Tumblr, see attached image.

This is an automated tweet, and will be repeated once per week. This tweet has been repeated {date_diff} times.
```

Please replace the tweet text and alt-text with the text of your choice, and provide an image if you are including one. The image adding and alt-text code, as well as the API v1 token code, should be removed if you are not attaching an image.

Remember to add your API keys, if `consumer_key`, `consumer_secret`, `access_token`, or `access_token_secret` are left blank, the script will not work. The script will also not work unless you set up OAuth 1.0a on your app, as your access token will be read-only.
