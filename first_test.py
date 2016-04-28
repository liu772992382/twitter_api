#!/usr/bin/env python
#coding=utf8
from myoauth import *
import json

CONSUMER_KEY = 'UAsW3M0DjQYC3xq7Pf7V4UE2A'
CONSUMER_SECRET = 'ugeOjlblJ40Q3wZgMsow9Q3IFJLewo5PZQgHH2D2CbaL0mK1sJ'
OAUTH_TOKEN = '724481025867284481-nQLPfe72TBd4xfG6yBRtIg1oNyELUpH'
OAUTH_TOKEN_SECRET = '1jURj276zpmKHOxUMRNuWJrQxAK2d22fKAkppNuYLENtu'

auth = twitter.oauth.OAuth(OAUTH_TOKEN,OAUTH_TOKEN_SECRET,CONSUMER_KEY,CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

print twitter_api

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

# print world_trends
# print
# print us_trends
# print json.dumps(world_trends,intent=1)

world_trends_set = set([trend['name'] for trend in world_trends[0]['trends']])
us_trends_set = set([trend['name']for trend in us_trends[0]['trends']])

common_trends = world_trends_set.intersection(us_trends_set) #

print common_trends
