import os
from dotenv import load_dotenv
import tweepy
import requests


def scrape_user_tweets(username, num_tweets=5, mock:bool = False):
    tweet_list = []
    twittergist = 'https://gist.githubusercontent.com/USD007/524f299b3f800b8003290dcd2439f144/raw/40b4bac532cc7b0c227d980b4dc753f432c67687/ujwal_d_twitter'
    tweets = requests.get(twittergist, timeout=5).json()
    if mock:
        twittergist = 'https://gist.githubusercontent.com/USD007/524f299b3f800b8003290dcd2439f144/raw/40b4bac532cc7b0c227d980b4dc753f432c67687/ujwal_d_twitter'
        tweets = requests.get(twittergist, timeout=5).json()
    else:
        print("twitter api is not free now")
    for tweet in tweets:
        tweet_dict = {}
        tweet_dict["text"] = tweet["text"]
        tweet_dict["url"] = f"https://twitter.com/{username}/status/{tweet['id']}"
        tweet_list.append(tweet_dict)

    return tweet_list

if __name__ == '__main__':
    tweets = scrape_user_tweets(username="ujwal d",mock= True)  #just a sample data here.
    print(tweets)