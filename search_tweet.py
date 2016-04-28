#!/usr/bin/env python
#coding=utf8
from myoauth import *
import json

q = '#NationalSuperheroDay' #搜索字符：也可以是关键字，推文发送者、推文相关地点

count = 100

search_results = twitter_api.search.tweets(q=q,count=count)

statuses = search_results['statuses']

for _ in range(5):
	print 'Length of statuses',len(statuses)
	try:
		next_results  = search_results['search_metadata']['next_results']
	except KeyError,e: # No more results
		break
#原程序无结果是会报错，使用try来catch错误就没问题
try:
	kwargs = dict([kv.split('=') for kv in next_results[1:].split('&')])
	search_results = twitter_api.search.tweets(**kwargs)#kwargs是字典
	statuses += search_results['statuses']

	print json.dumps(statuses[0],indent=1)
except NameError,e:
	print 'no result'


#1.4.1提取推文实体
t = statuses[0]

status_texts = [status['text'] for status in statuses]

screen_names = [user_mention['screen_name'] for status in statuses for user_mention in status['entities']['user_mentions']]

count=0

for status in statuses:
	print status['entities']['hashtags']
	for hashtag in status['entities']['hashtags']:
		print hashtag['text']

hashtags = [hashtag['text'] for status in statuses
								for hashtag in status['entities']['hashtags']]

words = [ w for t in status_texts for w in t.split()]

print json.dumps(status_texts[0:5],indent=1)
print json.dumps(screen_names[0:5],indent=1)
print json.dumps(hashtags[0:5],indent=1)
print json.dumps(words[0:5],indent=1)


#1.4.2用频率分析推文
from collections import Counter

for item in [words,screen_names,hashtags]:
	c = Counter(item)
	print c.most_common()[:10] #top 10
	print

#使用prettytable显示结果
from prettytable import PrettyTable

for label,data in(('Word',words),
					('Screen Name',screen_names),
					('Hashtag',hashtags)):
	pt = PrettyTable(field_names=[label,'Count'])
	c = Counter(data)
	[pt.add_row(kv) for kv in c.most_common()[:10]]
	pt.align[label],pt.align['Count'] = '1','r'
	print pt
