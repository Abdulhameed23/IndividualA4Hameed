import tweepy
import pandas as pd
import Twitterkeys as tw

client1 = tweepy.Client(bearer_token=tw.bearer_token, consumer_key=tw.consumer_key, consumer_secret= tw.consumer_secret, access_token=tw.access_token, access_token_secret=tw.access_token_secret)


def twitter(query):
    tweets = []
    response1 = client1.search_recent_tweets(query = query, max_results=10)
    for tweet in response1.data:
        tweets.append(tweet.text)
    df = pd.DataFrame({'tweets':tweets})
    return df

def account(name):
    tweets = []
    response1 = client1.get_user(username = name)
    id1 = response1.data.id

    response1 = client1.get_users_tweets(id1, max_results = 10)
    for tweet in response1.data:
        tweets.append(tweet.text)
    df = pd.DataFrame({'tweets':tweets})
    return df
