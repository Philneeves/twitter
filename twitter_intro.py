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

# This example will download your home timeline tweets and print each one of their texts to the console.
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text

# This example searches for trends by location (WOEID) and then shows common threads to both/all
DUB_WOE_ID = 560743
LON_WOE_ID = 44418
SYD_WOE_ID = 1105779

dub_trends = api.trends_place(DUB_WOE_ID)
lon_trends = api.trends_place(LON_WOE_ID)
syd_trends = api.trends_place(SYD_WOE_ID)

dub_trends_set = set([trend['name']
                      for trend in dub_trends[0]['trends']])

lon_trends_set = set([trend['name']
                      for trend in lon_trends[0]['trends']])

syd_trends_set = set([trend['name']
                      for trend in syd_trends[0]['trends']])

common_trends = set.intersection(dub_trends_set, lon_trends_set, syd_trends_set)

#print common_trends

#print json.dumps(dub_trends, indent=1)
#print json.dumps(lon_trends, indent=2)
print json.dumps(syd_trends, indent=3)