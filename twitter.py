import tweepy
import re
import urllib.request
from os import getcwd

from keys import *

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY,ACCESS_SECRET)
api = tweepy.API(auth)
#"https://twitter.com/Arsenal/status/1157984630135513091?s=20", have to figure out how to handle outliers like this url

#temporary list containing twitter urls for basic app.
#The actual model recieves these urls from the whatsapp bot. 
links = ["https://twitter.com/charles_watts/status/1157985584385859584?s=20"]


pattern = r"status/([\d]+)" #regex expression with capture group
id_list = [] #list of tweet id's

#looping through urls, extracting tweet ids and appending to id_list
for url in links:

	id=re.findall(pattern,url)[0] #id is type string 
	id_list.append(id)




#function that takes tweet-id as input, and returns image url from api
def find_media_url(id_string):
	tweet = api.get_status(id_string,tweet_mode='extended')
	if 'media' in tweet.entities:
		pic_url=tweet.extended_entities['media']
		return (pic_url[0]['media_url'])



image_url = find_media_url('1158341296437829633')
file_path = getcwd()+'/image.jpg'
urllib.request.urlretrieve(image_url,file_path)




"""
The following code is an alternate way to look up a list of ids (up to 100)

#pass in the ids as a list, and tweet_mode is set to extended to get the entities
tweets = api.statuses_lookup(id_list,tweet_mode='extended')


for tweet in tweets:

	count +=1
	print(count)

	if 'media' in tweet.entities:
		for image in tweet.extended_entities['media']:
			print(image['media_url'])

"""
	
