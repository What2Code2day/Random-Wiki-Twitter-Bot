
from nturl2path import url2pathname
import requests
from bs4 import BeautifulSoup
import tweepy
import time


# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER",
                           "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN",
                      "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)

# Create a tweet and prints one every 10min
while True:
    get_url = "https://en.wikipedia.org/wiki/Special:Random"
    u = requests.get(get_url)
    soup = BeautifulSoup(u.content, 'html.parser')
    title = soup.find(class_="firstHeading").text
    url = 'https://en.wikipedia.org/wiki/%s' % title
    title = soup.find(class_="firstHeading").text
    fixed_url = url.replace(" ", "_")
    print(fixed_url)
    api.update_status(fixed_url)
    time.sleep(10*60)
