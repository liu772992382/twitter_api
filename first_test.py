#!/usr/bin/env python
#coding=utf8
import twitter

CONSUMER_KEY = 'UAsW3M0DjQYC3xq7Pf7V4UE2A'
CONSUMER_SECRET = 'ugeOjlblJ40Q3wZgMsow9Q3IFJLewo5PZQgHH2D2CbaL0mK1sJ'
OAUTH_TOKEN = '724481025867284481-nQLPfe72TBd4xfG6yBRtIg1oNyELUpH'
OAUTH_TOKEN_SECRET = '1jURj276zpmKHOxUMRNuWJrQxAK2d22fKAkppNuYLENtu'

auth = twitter.oauth.OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

print twitter_api