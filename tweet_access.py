import json
import tweepy
from tweepy import OAuthHandler

# Replace these values with our own twitter app settings
CONSUMER_KEY = 'k6U2nPJhwYp45zVkC03II2tcm'
CONSUMER_SECRET =   'hffPKBt1vEdSjz6WdGMdL5ECTkoGBPpLadptVZcfPXEGPzHdSJ'
OAUTH_TOKEN = '361613339-mYmihUb7TTLXVGFJg90O4NV03oXKQ9OYO8XGzI6T'
OAUTH_TOKEN_SECRET = 'EDX2ajUMX7Y5DlqcYWfRuCu0Hscw5LH5J5A9wrQNPL3B4'

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

count = 10
query = 'London'

# Get all statuses (stati?)
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]
print json.dumps(results[0]._json, indent=4)

for status in results:
    print status.text.encode('utf-8')
    print status.user.id
    print status.user.screen_name
    print status.user.profile_image_url_https
    print status.user.followers_count
    print status.place

    # print results
    # returns results in long string