# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 11:58:03 2020

@author: aparn
"""

import tweepy as tw
import preprocessor as p
import speech_recognition as sr
from googletrans import Translator
from random import random
import gtts
from playsound import playsound

# Neccessary credentials required to aunthenticate the connection to access twitter from the API.
#bhavana
access_token = '1323310247331745792-Kp7vyZWX39Mcm7KDW04HqKfDNGwWN4'
access_secret = 'IQHLiLYVUMxMsJ5pBZRDIarOuxuOQ3FKlvA614sXarv8g'
consumer_key = 'aXUDhNT3iore12pK9hKU0oJXN'
consumer_secret = 'TLo5Mq0PBIJSARrs1cGdLqSmmv4v3QddHW7bZvbl8ltq6PkwD6'

authorize = tw.OAuthHandler(consumer_key, consumer_secret)
authorize.set_access_token(access_token, access_secret)
api = tw.API(authorize)

# create a speech recognition object
r = sr.Recognizer()
##get voice input
with sr.Microphone() as source:
    # read the audio data from the default microphone
    print("Say Something...")
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    
# Define the search term and the date_since date as variables
search_words = "#"+text
#print(search_words)

tweets = api.search(search_words,count=2)
tweets_text = [tweet.text for tweet in tweets]
print(tweets_text)
p.set_options(p.OPT.URL, p.OPT.EMOJI)
filtered_tweets = [p.clean(tweet) for tweet in tweets_text]
filtered_tweet_list = [w.replace('|', '') for w in filtered_tweets]
print(filtered_tweet_list)

#translation
#print(googletrans.LANGUAGES)
translator = Translator()
result = translator.translate(filtered_tweet_list, dest='hi')
tweets_translated = [trans.text for trans in result]
trans_text = ''
for tweet in tweets_translated:
    trans_text+=tweet
    trans_text+="."
print(trans_text)

#generate audio
tts = gtts.gTTS(trans_text, lang="hi", slow=False)
file_number = "tweets"+str(random())+".mp3" 
tts.save(file_number)
playsound(file_number)

