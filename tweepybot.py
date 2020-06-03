import tweepy, os, time, sys
from random import randint
from spok import *

dependencies = ['CONSUMER_KEY', 'CONSUMER_SECRET', 'ACCESS_KEY', 'ACCESS_SECRET', 'DELAYTIME']

fl = open('key.txt', 'r')
key = [line.strip() for line in fl]
        
for i in range(len(dependencies)):
    dependencies[i] = str(key[i])

CONSUMER_KEY = str(dependencies[0])
CONSUMER_SECRET = str(dependencies[1])
ACCESS_KEY = str(dependencies[2])
ACCESS_SECRET = str(dependencies[3])
delayTime = int(dependencies[4])

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def updatestatus():
    tweet = subjek[randint(0, len(subjek)-1)]+predikat[randint(0, len(predikat)-1)]+objek[randint(0, len(objek)-1)]+keterangan[randint(0, len(keterangan)-1)]+' -Bot'
    api.update_status(tweet)
    print('TWEET POSTED')
    time.sleep(delayTime)
    if tweepy.error.TweepError:
        os.system('clear')
        print('FAILED TO POST')

while True:
    updatestatus()


