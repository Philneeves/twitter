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

count = 50
query = 'Dublin'

# Get all tweets for the search query
results = [status for status in tweepy.Cursor(api.search, q=query).items(count)]

status_texts = [status._json['text'] for status in results]

screen_names = [status._json['user']['screen_name']
                for status in results
                for mention in status._json['entities']['user_mentions']]

hashtags = [hashtag['text']
            for status in results
            for hashtag in status._json['entities']['hashtags']]

words = [word
         for text in status_texts
         for word in text.split()]

print json.dumps(status_texts[0:5], indent=1)
print json.dumps(screen_names[0:5], indent=1)
print json.dumps(hashtags[0:5], indent=1)
print json.dumps(words[0:5], indent=1)