import tweepy, time, sys
from random import randint
from spok import *
#token API di sini
#There's API Key, from twitter.developer
CONSUMER_KEY = 'CONSUMERKEYMILIKMU'
CONSUMER_SECRET = 'CONSUMERKEYSECRETMILIKMU'
ACCESS_KEY = 'ACCESSKEYMILIKMU' 
ACCESS_SECRET = 'ACCESKEYSECRETMILIKMU'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

while True:
    api.update_status(subjek[randint(0, len(subjek)-1)]+predikat[randint(0, len(predikat)-1)]+objek[randint(0, len(objek)-1)]+keterangan[randint(0, len(keterangan)-1)]+' -Bot')
    time.sleep(86400)
    #jeda antar twit dalam satuan detik
    #pauses between twit in second
